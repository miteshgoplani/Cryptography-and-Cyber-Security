
def encryption(ptxt,k,ch):
	ptxt = ptxt.lower()
	#plain is list of alphabets 
	plain = list(ptxt)
	#p is list of corresponding nos for plaintext	
	p = [ord(x)-97 for x in plain]  
	c = []
	cipher = []
	#Caesar Cipher	
	if(ch==1): 
		for i in range(0,len(p)):
			c.append((p[i]+k)%26)
			cipher.append(chr(c[i]+97))
		ctxt = ''.join(cipher)
		ctxt = ctxt.upper()
		return ctxt
	
	#Autokey Cipher
	if(ch==2):
		c.append((p[0]+k)%26)
		cipher.append(chr(c[0]+97))
		for i in range(1,len(p)):
			c.append((p[i]+p[i-1])%26)
			cipher.append(chr(c[i]+97))
		ctxt = ''.join(cipher)
		ctxt = ctxt.upper()
		return ctxt


def decryption(ctxt,k,ch):
	ctxt = ctxt.lower()
	#cipher is list of alphabets
	cipher = list(ctxt)
	#c is list of corresponding nos for ciphertext	
	c = [ord(x)-97 for x in cipher]
	p = []
	plain = []
	#Caesar Cipher
	if(ch==1):
		for i in range(0,len(c)):
			p.append((c[i]-k)%26)
			plain.append(chr(p[i]+97))
		ptxt = ''.join(plain)
		return ptxt

	#Autokey Cipher
	if(ch==2):
		p.append((c[0]-k)%26)
		plain.append(chr(p[0]+97))
		for i in range(1,len(c)):
			p.append((c[i]-p[i-1])%26)
			plain.append(chr(p[i]+97))
		ptxt = ''.join(plain)
		return ptxt
	


ptext = input("Enter plain text: ")
ptext.replace(' ','')
print("1.Caesar Cipher\n2.Autokey Cipher")
choice = int(input("Enter the choice of cipher: "))
key = int(input("Enter key: "))

ciphertext = encryption(ptext,key,choice)
print("Cipher Text is: "+ciphertext)

plaintext = decryption(ciphertext,key,choice)
print("Plain Text is: "+plaintext)

