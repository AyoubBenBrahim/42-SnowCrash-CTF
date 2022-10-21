while looking for flag00 in level00

cat /etc/passwd
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash

crack the passwd file using John the Ripper

download john https://download.openwall.net/pub/projects/john/contrib/macosx/

echo "42hDRfypTqqnw" > level01
./run/john level01 --show 
passwd = abcdefg
su flag01 
getflag
token : f2av5il02puano7naaf6adaaf
