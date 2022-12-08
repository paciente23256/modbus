#! /usr/bin/env python

# Bibliotecas
from scapy.all import *
from scapy import *
from scapy.utils import rdpcap
from scapy.utils import wrpcap
import runpy

# Le o ficheiro pcap original
packets = rdpcap("modbus.pcap", 1000)

for pkt in packets:
    if pkt.haslayer(Raw) == 1:
        #manipulacao do data raw hex referente aos holding registers -  \x00\x64 -> 100
        pkt[0][Raw].load ="\x00{\x00\x00\x00\x17\x01\x03\x14\x00\x64\x00\x64\x00\x64\x00\x64\x00\x64\x00\x64\x00\x64\x00\x64\x00\x64\x00\x64"

        """ muda o registos aleatoriamente e cria o padding layer 
        pkt[0][Raw].load ="\x00{\x00\x00\x00\x17\x01\x03\x14\x28\xB8\\x28\xB8\x28\xB8\x28\xB8\x28\xB8\x28\xB8\x28\xB8\x28\xB8\x28\xB8\x28\xB8"
        """

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
# Imprimi o resultado
for pkt in packets:
   pkt.display()

# escreve novo pcap
wrpcap("new_registers.pcap", packets)

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
