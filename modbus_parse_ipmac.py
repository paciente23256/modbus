import scapy.all as scapy
import scapy.contrib.modbus as mb

import os, sys, time, subprocess, runpy
from subprocess import call


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
|    IPBEJA - MESI - CIC - M0dBus     |
|                                     |
\033[37;40m|   -=   inject Pcap Modbus TCP   =-  |
|                                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Alunos: #23258  &   # 23256     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   """)


for pkt in scapy.PcapReader("new_ip_mac.pcap"):
    if mb.ModbusADUResponse in pkt:
        pkt.show()



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
