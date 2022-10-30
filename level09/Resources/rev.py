import sys

n = len(sys.argv[1])

for elem in range(0, n):
   print(chr(ord(sys.argv[1][elem]) - elem), end = '')
