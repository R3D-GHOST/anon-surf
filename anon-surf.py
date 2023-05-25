import os
import time

banner = """
 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗      ███████╗██╗   ██╗██████╗ ███████╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║      ██╔════╝██║   ██║██╔══██╗██╔════╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║█████╗███████╗██║   ██║██████╔╝█████╗  
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║╚════╝╚════██║██║   ██║██╔══██╗██╔══╝  
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║      ███████║╚██████╔╝██║  ██║██║     
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝      ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     
                                                                            
"""
    
def menu():
    os.system('clear')
    print('R3D-GHOST')
    print('')
    print('starting anon-tor')
    time.sleep(1)
    os.system('clear')
    banner
    print('')
    print('1 --> Start Anon-Surf')
    print('')
    print('2 --> Stop Anon-Surf')
    print('')
    print('3 --> Exit Script')
    print('')
    opt = input("--> ")
    
    if opt == "1":
        start()
    elif opt == "2":
        stop()
    elif opt == "3":
        exit()

def start():
    os.system('clear')
    print('1) Arch Linux')
    print('')
    print('2) Debian')
    print('')
    start = input("--> ")
    if start == "1":
        os.system('sudo systemctl enable --now tor.service')
        os.system('ss -nlt')
        os.system('wget -qO - https://api.ipify.org; echo')
        os.system('torsocks wget -qO - https://api.ipify.org; echo')
        os.system('source torsocks on')
        time.sleep(2)
        os.system('clear')
        os.system('proxychains torbrowser-launcher')
    elif start == "2":
        os.system('sudo service tor start') 
        os.system('sudo service tor status')
        time.sleep(2)
        os.system('clear')
        os.system('proxychains torbrowser-launcher')
     
    
    
def stop():
    os.system('sudo service tor stop')
    os.system('systemctl stop tor.service')
    
menu()