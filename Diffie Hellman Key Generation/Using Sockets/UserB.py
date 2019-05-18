import socket

import random
import time

def select_private_keys(p):

 a = random.randrange(1,p)

 return a
if __name__ == '__main__':
 host = socket.gethostname()
 

 port = 5000
 userB_socket = socket.socket()

 userB_socket.connect((host, port))
 while True:
   g = userB_socket.recv(1024).decode()
   if not g:
      break

   g = int(g)
  
   p = int(userB_socket.recv(1024).decode())

   print("g and p received")

   time.sleep(2)
   y = select_private_keys(p)

   r2 = pow(g, y, p)

   r1 = int(userB_socket.recv(1024).decode())

   print("r1 received")

   time.sleep(2)
   userB_socket.send(str(r2).encode())

   print("r2 sent")

   time.sleep(2)
   k1 = int(userB_socket.recv(1024).decode())

   print("k1 received")

   time.sleep(2)
   k2 = pow(r1, y, p)

   userB_socket.send(str(k2).encode())

   print("k2 sent")

   time.sleep(2)
   #k1=5
   if k1 == k2:
    print("Both are equal")

   else:
    print("Both are not equal")

userB_socket.close()

 
