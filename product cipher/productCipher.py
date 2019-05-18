#Caesar Cipher then Simple substitution Cipher
import random
def Caesarencryption(ptxt,k):
    ptxt = ptxt.lower()
    #plain is list of alphabets 
    plain = list(ptxt)
    #p is list of corresponding nos for plaintext	
    p = [ord(x)-97 for x in plain]  
    c = []
    cipher = []
    for i in range(0,len(p)):
        c.append((p[i]+k)%26)
        cipher.append(chr(c[i]+97))
    ctxt = ''.join(cipher)
    ctxt = ctxt.upper()
    return ctxt


def Caesardecryption(ctxt,k):
    ctxt = ctxt.lower()
    #cipher is list of alphabets
    cipher = list(ctxt)
    #c is list of corresponding nos for ciphertext	
    c = [ord(x)-97 for x in cipher]
    p = []
    plain = []
    for i in range(0,len(c)):
        p.append((c[i]-k)%26)
        plain.append(chr(p[i]+97))
    ptxt = ''.join(plain)
    return ptxt


alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '

def substitutionMakeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def substitutionEncrypt(plaintext, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def substitutionDecrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)

ptext = input("Enter plain text: ")
ptext.replace(' ','')
print("Product Cipher - Caesar and Substitution")
key = int(input("Enter key for caesar cipher:"))
cipher1 = Caesarencryption(ptext,key)
print("Encryption level 1(Caesar): "+cipher1)

subkey = substitutionMakeKey(alphabet)
print("Key for substitution Cipher ",subkey)
cipher2 = substitutionEncrypt(cipher1, subkey, alphabet)
print("Encryption level 2(substitution): ",cipher2)

print()

dec1 = substitutionDecrypt(cipher2, subkey, alphabet)
print("Decryption level 1(Substitution): ",dec1)

plaintext = Caesardecryption(dec1,key)
print("Decryption level 2(Caesar): "+plaintext)

