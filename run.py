import os, sys, time, subprocess, runpy
from subprocess import call




def ip_mac():
        runpy.run_path(path_name='modbus_ip_mac.py')
def registos():
        runpy.run_path(path_name='modbus_registers.py')
def ver_ip_mac():
        runpy.run_path(path_name='modbus_parse_ipmac.py')
def ver_reg():
        runpy.run_path(path_name='modbus_parse_reg.py')
def ver_ori():
        runpy.run_path(path_name='modbus_parse.py')


#BANNER MENU
def menu():
        print ("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
        print("=> MENU INCIAL")
        time.sleep(1)
        print()
        choice = input("""
[1] - Modbus - Ver Pcap Original
[2] - Modbus - Inject IPs e Mac
[3] - Modbus - Inject Mul. Holding Registers
[4] - Modbus - Ver Pcap IPs&Macs Manipulados
[5] - Modbus - Ver Pcap Registers Manipulados 

[0] - Sair

        \033[1;33;40m

\033[1;34;40m\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n
\033[37;40m
""")

        if choice == "[1]" or choice == "1":
                ver_ori()
        elif choice == "[2]" or choice == "2":
                ip_mac()
        elif choice == "[3]" or choice == "3":
                registos()
        elif choice == "[4]" or choice == "4":
                ver_ip_mac()
        elif choice == "[5]" or choice == "5":
                ver_reg()
        elif choice == "[0]" or choice == "0":
                print("+ Saiu do Programa.")
                sys.exit()
        else:
                print("+ Por favor seleccione uma opção válida.")
                print("+ Tente novamente.")
                menu()

if __name__ == '__main__':
        subprocess.call('clear', shell=True)

"""
BANNER
"""
print("""\033[1;34;40m

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                |
|          IPBEJA - MESI - CIC - M0dBus          |
|                                                |
\033[37;40m|         -=   inject Pcap Modbus TCP   =-       |
|                                                |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Alunos: #23258  &   # 23256            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   """)

menu()
