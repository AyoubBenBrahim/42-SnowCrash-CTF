
on the host machine:
```
scp -P 4242 level02@10.12.100.237:/home/user/level02/level02.pcap $HOME/Desktop/snow-crash/level02/Resources
```

pass = f2av5il02puano7naaf6adaaf

`chmod 777 level02.pcap`

resend it to a VM where Wireshark is installed
```
scp $HOME/Desktop/snow-crash/level02/Resources/level02.pcap mohamed@10.12.100.190:/home/mohamed/Desktop
```
To load a PCAP file in Wireshark, open Wireshark and in the menu bar, click ‘File’, then click ‘Open’ and navigate to the file’s location, then click ‘Open.’

Analyze -> Follow -> TCP stream 
copy the section after the occurance of "Passw ord" which states in plain Text format:

`ft_wandr...NDRel.L0L`
-> show data as Hex Dump: 

66 74 5f 77 61 6e 64 72 7f 7f 7f 4e 44 52 65 6c 7f 4c 30 4c 0d

copy into a [Hex decoder](https://cryptii.com/pipes/hex-decoder)

ft_wandr:x::x::x:NDRel:x:L0L ==> ft_waNDReL0L

su flag02
getflag => kooda2puivaav1idi4f57q8iq




