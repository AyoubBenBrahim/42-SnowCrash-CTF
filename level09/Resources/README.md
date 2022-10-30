ssh level09@ip -p 4242
password: 25749xKZ8L7DkSCwJkT9dyv6f


ll

level09@SnowCrash:~$ ./level09
You need to provied only one arg.

level09@SnowCrash:~$ ./level09 123456
13579;

1 + 0 = 1
2 + 1 = 3
3 + 2 = 5
4 + 3 = 7
5 + 4 = 9
6 + 5 = ;


#include<stdio.h>
#include<string.h>

int main(int ac, char** av)
{
	for (int i = 0; i < strlen(av[1]); i++)
	{
		printf("%c" ,av[1][i] - i);
	}
	printf("\n");
	return (0);
}

gcc -std=c99 /tmp/decode.c
./a.out $(cat /home/user/level09/token)

su flag09

flag09@SnowCrash:~$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z

