import string

alphabet = list(string.ascii_lowercase*2)
print(alphabet)
line = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
       "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
lst =[]
for symbol in line:
    if symbol in alphabet:
        lst.append(alphabet[alphabet.index(symbol)+2])
    else:
        lst.append(symbol)
print("".join(lst))

