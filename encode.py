PLAIN=input("what?")
KEY=3
enc=""
for char in list(PLAIN):
    ASCII=ord(char)
    num=ASCII-97
    num=(num-KEY)%26
    ASCII=num+97
    enc+=chr(ASCII)
print(enc)