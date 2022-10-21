
we are at `/home/user/level03`

In the home we found a binary file `level03`

first thing to notice when `ls`-ing the dir are the file permissions:
`rwsr-sr-x`
**owner**: has read, write, [SUID permissions](https://www.zzee.com/solutions/linux-permissions.shtml)
**group**: read and SGID permissions

```the setguid bit set = if the file were executed, that it would be run with the effective rights of the group owner (instead of that of the user who executed it). On a directory, the setgid bit means that, if a file is created in the directory, its group-owner would be that of the directory (instead of that of the user who created it).```

if we execute `./level03`, it outputs the msg: `Exploit me`