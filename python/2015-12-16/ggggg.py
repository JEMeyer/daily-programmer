import sys

fo = open(sys.argv[1], 'r')
d = fo.readLine()
codeCrack = dict(zip(d[0::2], d[1:2]))
message = fo.readLine()
fo.close()

print(codeCrack)
print(message)