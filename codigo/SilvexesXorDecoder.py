import fileinput
from itertools import cycle

def xor(var, key):
    return bytes(a ^ b for a, b in zip(var, cycle(key)))

o = open("decodedSilvexes", "xb")
key = b'MJQDKXK6B37PBGJ42XD6ARPFLIU37'

f = open("silvexes", "rb")
input = f.read(-1)
output = xor(input, key)
o.write(output)