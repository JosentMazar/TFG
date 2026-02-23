var1 = 0x385b7bd9
var2 = 0x68d23ef5
print(var1)
print(var2)
key = 0x0
piece = ""
file1 = open("encrypted3.txt", "r")
file2 = open("dencrypted2.txt", "w")

text1 = file1.readlines()
text1 = text1[0]


while len(text1) > 7:
    
    key = key * var1
    print(key)
    key = hex(key)
    key = int(key[2:10], 16)
    key = key + var2
    print(key)
    key = hex(key)
    key = int(key[2:10], 16)
    print(key)
    piece = text1[0:8]
    print(piece)
    piece = int(piece, 16)
    print(piece)
    text1 = text1[8:]
    piece = piece ^ key
    print(hex(piece)[2:])
    file2.write(hex(piece)[2:])
    
    
