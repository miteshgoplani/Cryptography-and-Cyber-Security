import random

alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
plaintext = "Hey, this is really fun!"


def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(plaintext, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    #print(keyMap)
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def decrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)

key = makeKey(alphabet)
print(key)
cipher = encrypt(plaintext, key, alphabet)
print(plaintext)
print(cipher)
print(decrypt(cipher, key, alphabet))