#program to create an encrypted and decrypted string by embedding a short symbol based string after each character

def encrypt(sttr,enkey):
    return enkey.join(sttr)

def decrypt(sttr,enkey):
    return sttr.split(enkey)

#main
mainString = input("Enter a string: ")
encryptStr = input("Input encryption key: ")
enStr = encrypt(mainString,encryptStr)
deLst = decrypt(enStr,encryptStr)
#deLst is in the form of a list, cpnverting it to string below
deStr = "".join(deLst)
print("The encrypted string is", enStr)
print("The decrypted string is", deStr)