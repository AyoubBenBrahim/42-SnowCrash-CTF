ssh level01@10.12.100.98 -p 4242
pwd: x24ti5gi3x0ol2eh4esiuxias

while looking for flag00 in level00
```
cat /etc/passwd

grep flag01 /etc/passwd

flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
```
crack the passwd file using John the Ripper

[download john](https://download.openwall.net/pub/projects/john/contrib/macosx/)
```
echo "42hDRfypTqqnw" > level01
./run/john level01 --show 
```
passwd = `abcdefg`

su flag01 
getflag
token : **f2av5il02puano7naaf6adaaf**

/etc/passwd vs /etc/shadow

20 years ago or so, most Unix variants shifted from keeping hashed passwords in the /etc/passwd file and moved them to /etc/shadow.
The reason for this was that /etc/passwd needed to be world readable for tools like 'finger' and 'ident' to work.
 Once passwords were segregated into /etc/shadow, that file was made readable only by root.

 https://security.stackexchange.com/questions/92766/what-can-hackers-do-with-ability-to-read-etc-passwd

