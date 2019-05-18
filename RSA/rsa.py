import math
p = int(input("Enter first prime no: "))
q = int(input("Enter second prime no: "))
n = p*q
phi_n = (p-1)*(q-1)
print("phi_n is:",end=" ")
print(phi_n)
# d is multiplicative inverse of e in phi_n
def modInv(a,x):
	a = a % x; 
	for i in range(1, x): 
		if ((a * i) % x == 1): 
			return i 
def coprime(a):
	list1 = []
	for x in range(2,a):
		if(math.gcd(a,x)==1 and modInv(x,phi_n)!=None):
			list1.append(x)
	for x in list1:
		if x is modInv(x,phi_n):
			list1.remove(x)
	return list1
list2 = coprime(phi_n)
print("Select a key from the coprime list: ")
print(list2)
e = int(input("e is: "))
d = modInv(e,phi_n)
print("Public key is: ",end=" ")
print("("+str(e)+","+str(phi_n)+")")
print("Private key is: ",end=" ")
print("("+str(d)+","+str(phi_n)+")")
print("Enter plain text: ", end=' ')
p = int(input())
c = (p**e)%n
print("Encrypted text is: "+str(c))

print()
print("Enter cipher text: ",end=' ')
c = int(input())
p = (c**d)%n
print("Decrypted text is: "+str(p))
