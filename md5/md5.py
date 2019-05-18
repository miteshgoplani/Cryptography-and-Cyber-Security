import hashlib
import time

string = "Hello Mitesh Goplani"

t1=time.clock()

result = hashlib.md5(string.encode()) 

t2=time.clock()  

print("The hexadecimal equivalent of hash is : ", end ="")

print(result.hexdigest())

print("Processing time: ", t2-t1)


a = hashlib.md5('Hi'.encode()).hexdigest()
b = hashlib.md5('Ho'.encode()).hexdigest()
diff = sum( a[i] != b[i] for i in range(len(a)) )
print(diff*4,diff*4/128*100)

a = hashlib.md5('CSS'.encode()).hexdigest()
b = hashlib.md5('DSS'.encode()).hexdigest()
diff = sum( a[i] != b[i] for i in range(len(a)) )
print(diff*4,diff*4/128*100)