
import socket

import random

import time

def select_private_keys(p): 
	a = random.randrange(1,p) 
	return a

def primitive_root(g, p):

 residual_set = []

 for i in range(1,p):

  residual_set.append(i)

# print(residual_set)

 temp_set = []

 for j in range(1,p): 
 		temp = pow(g, j, p) 
 		temp_set.append(temp)

 temp_set.sort()

 if temp_set != residual_set:

  return False

 else:

  return True

if __name__ == '__main__': 
 host = socket.gethostname() 
 port = 5000

 userA_socket = socket.socket()

 userA_socket.bind((host, port))

 userA_socket.listen(2)

 conn, address = userA_socket.accept()

 print("connected to : ",str(address))

 g = int(input("Enter g : "))

 p = int(input("Enter p : "))
 







if(primitive_root(g, p)):

 print(g, " is primitive root of ", p)

 conn.send(str(g).encode())

 conn.send(str(p).encode())

 print("g and p sent")

 time.sleep(2)

 x = select_private_keys(p)

 r1 = pow(g, x, p)

 conn.send(str(r1).encode())

 print("r1 sent")

 time.sleep(2)

 r2 = int(conn.recv(1024).decode())

 print("r2 received")

 time.sleep(2)

 k1 = pow(r2, x, p)

 conn.send(str(k1).encode())

 print("k1 sent")

 time.sleep(2)

 k2 = int(conn.recv(1024).decode())

 print("k2 received")

 time.sleep(2)

 if k1 == k2:

  print("Both are equal")

 else:

  print("Both are not equal")

 conn.close()

else:

 print(g, " is not primitive root of ", p)

 conn.close()
