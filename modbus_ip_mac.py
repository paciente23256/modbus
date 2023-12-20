#!/usr/bin/env python

#bibliotecas
import scapy.contrib.modbus as mb
from scapy.all import *
from scapy.utils import rdpcap
from scapy.utils import wrpcap
import os, sys, time, subprocess, runpy
from subprocess import call

# define ficheiros pcap (in|out) 
packets = rdpcap('modbus.pcap')
new_cap = PcapWriter("new_ip_mac.pcap")

# variaveis IP e Mac
srcIp=packets[0][IP].src
dstIP=packets[0][IP].dst
srcMac=packets[0][Ether].src
dstMac=packets[0][Ether].dst

# definicao de novos IP & Macs 
ip1='8.8.8.8'
ip2='1.1.1.1'
mac1='00:0c:29:ba:6c:00'
mac2='00:0c:29:ba:6c:01'

# substitui os IPs src dst originais
for pkt in packets:

    if(pkt[IP].src == srcIp):
        pkt[IP].src = ip1
    elif(pkt[IP].src == dstIP):
        pkt[IP].src = ip2
    if(pkt[IP].dst == srcIp):
        pkt[IP].dst = ip1
    elif(pkt[IP].dst == dstIP):
        pkt[IP].dst = ip2

# substituicao os Macs src dst originais
    if(pkt[Ether].src == srcMac):
        pkt[Ether].src = mac1
    elif(pkt[Ether].src == dstMac):
        pkt[Ether].src = mac2
    if(pkt[Ether].dst == srcMac):
        pkt[Ether].dst = mac1
    elif(pkt[Ether].dst == dstMac):
        pkt[Ether].dst = mac2

# reescreve pcap
    new_cap.write(pkt)

def go_menu():
        runpy.run_path('run.py')



if __name__ == '__main__':
        subprocess.call('clear', shell=True)

"""
BANNER
"""
print("""\033[1;34;40m

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                     |
|                                     |
\033[37;40m|   -=   inject Pcap Modbus TCP   =-  |
|                                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

   """)


# imprime
for pkt in packets:
   pkt.display()


print("""\033[1;33;40m

      """)

print("\033[1;34;40m\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

choice = input("""\033[37;40m
1 - Menu Inicial
0 - Sair
""")

if choice == "1" or choice == "menu principal":
        go_menu()


elif choice == "0" or choice == "sair":
        print("+ Saiu do programa.")
        sys.exit()

else:
        print("+ Por favor seleccione uma opção válida.")
        print("+ Tente novamente.")
