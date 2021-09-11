import re,os
import time
import subprocess
import urllib.request
import urllib.parse
import sys
from os import system
from platform import platform
from time import sleep
import os
import random



class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
class Script:
    series = [""]*10
    os.system('clear')
    print(color.END+"Connecting internet...")
    try:
        urllib.request.urlopen('https://www.google.com')
        os.system('clear')
        print(color.GREEN+"Ok"+color.END)
    except:
        os.system('clear')
        print(color.RED+"Connecting ERROR"+color.END)
        input('Нажмитe Enter, чтобы выйти...')
        exit()
    time.sleep(1)
    def menu(self):
        
        os.system('clear')
        print("Terrax v.1\n")
        print("[1]. Установить/Обновить пакеты")
        print("[2]. Установить/Обновить Metasploit")
        print("[3]. Установить/Обновить Sms-Bomber")
        print("[4]. Установить/Обновить PhoneInfo")
        print("\n[0]. exit")
        
        print("\n~~~~~~~~~~~~~~~~~~")
        try:
            file2 = open("log.txt", "r")
            while True:
                line = file2.readline()
                    
                if not line:
                    break
                print(line.strip())
            file2.close()
        except:
            pass
        print("~~~~~~~~~~~~~~~~~~")
        inp = input('~~=> ')
        
        
        if inp == '0':
            print("\t~~~~ Пока ~~~~")
        if inp == 'q':
            print("\t~~~~ Пока ~~~~")
        if inp == '1':
            file1 = open("pkgs.ini", "r")
            file2 = open("log.txt", "w")
            file2.write('Starting update...'+'\n')
            while True:
                line = file1.readline()
                if not line:
                    break
                os.system(line.strip())
                file2.write(line.strip()+'\n')
            file2.write('Done'+'\n')
            file1.close()
            file2.close()
            os.system('clear')
            
            self.menu()
        if inp == '2':
            file1 = open("Metasploit.ini", "r")
            file2 = open("log.txt", "w")
            file2.write('Downloading Metasploit...'+'\n')
            while True:
                line = file1.readline()
                if not line:
                    break
                os.system(line.strip())
                file2.write(line.strip()+'\n')
            file2.write('Done'+'\n')
            file1.close()
            file2.close()
            os.system('clear')
            
            self.menu()
        if inp == '3':
            file1 = open("sms-bomber.ini", "r")
            file2 = open("log.txt", "w")
            file2.write('Downloading Sms-Bomber...'+'\n')
            while True:
                line = file1.readline()
                if not line:
                    break
                os.system(line.strip())
                file2.write(line.strip()+'\n')
            file2.write('Done'+'\n')
            file1.close()
            file2.close()
            os.system('clear')
            
            self.menu()
MainCode=Script()
MainCode.menu()