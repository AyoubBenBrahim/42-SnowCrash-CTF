
as usual: su level05
Reconnaissance, Enumeration, nothing interesting encountered

ssh level05@10.12.100.98 -p 4242
level05's password: ne2searoevaevoem4ov4ar8ap
You have new mail.

quick google search: "linux mail path" gives the path of mails dir 

cat /var/spool/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05

its a crontab apparantley
that runs At every 2nd minute, [check](https://crontab.guru/#*/2_*_*_*_*)

heading back to the path
```
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

ulimit is a built-in Linux shell command that allows viewing or limiting system resource amounts that individual users consume. Limiting resource usage is valuable in environments with multiple users and system performance issues.

-t flag: Specifies a process's maximum running time, in seconds.

bash -x: The -x option starts a BASH shell in tracing mode.
	run the entire script in debug mode. Traces of each command

 echo "getflag > /tmp/flag"
watch cat /tmp/flag


