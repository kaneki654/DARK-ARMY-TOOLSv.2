import os
import random
import sys
import time
import pyfiglet
from functionality.drkrmydnction import clear

class colors:
    RAWR = '\033[91m'
    TAE = '\033[92m'

print(colors.RAWR + "WAIT MO LANG YA, BILANG KA LIMA..")
time.sleep(5)
clear()

ascii_banner = pyfiglet.figlet_format("DARK-ARMY-DDOS-TOOLS")
print(ascii_banner)

print(colors.TAE + '[1]DDOSit')
print(colors.RAWR + '[2]C2')
print(colors.TAE + '[3]BYPASSES')
print(colors.TAE + '[4]CRYPTOR')
print(colors.RAWR + '[5]DDOSSAMP')
print(colors.RAWR + '[6]403')
print('[7]SQLMAP')
print('[8]SETOOLKIT')

user_input = int(input('PILI KA ISA YA: '))


if user_input == 1:
        clear()
        
        ascii_banner = pyfiglet.figlet_format('DDOSit')
        print(ascii_banner)

        print('[1]GRAA')
        print('[2]FLOOD')

        user_input = int(input('PILI KPA ISA RAWR: '))
        if user_input == 1:
            from DDOSit.GRAA import *
            import subprocess

            cmd = 'python GRAA.py'
            p=subprocess.Popen(cmd,shell=True)
            NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
            print(BOBO_ERROR_HAHAHAH_KAWAWA)
            print(NAG_OUT_TANGINANG_YAN)

        else:
            print('RAWR error')
            quit()

        if user_input == 1:
            from DDOSit import *
            import subprocess
            
            print('type [go build httpflood.go]')

            user_input = int(input('TYPE IT RIGT HERE: '))

            try:
                if user_input == 'go build httpflood.go':
                    cmd = './httpflood.go'
                    p=subprocess.Popen(cmd,shell=True)
                    NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
                    print(BOBO_ERROR_HAHAHAH_KAWAWA)
                    print(NAG_OUT_TANGINANG_YAN)
        
            except:
                print('ayusing mo typings mo')
                quit()

if user_input == 2:
    clear()

    ascii_banner = pyfiglet.figlet_format('C2')
    print(ascii_banner)
    
    print('[1]ZXCDDOS')

    user_input = int(input('PILI KA BAI: '))

    if user_input == 1:
        from C2.POWPOW import *
        import subprocess

        cmd = 'python POWPOW.py'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)

    else:
        print('BOOM error HAHHAHAHHA')
        quit()

if user_input == 4:
    clear()

    ascii_banner = pyfiglet.figlet_format('CRYPTOR')
    print(ascii_banner)

    print('[1]C2 CRYPTOR')
    
    user_input = int(input('PILI KA PA DITO BAI: '))

    if user_input == 1:
        from CRYPTOR.simulan import *
        import subprocess

        cmd = 'python simulan.py'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    
    else:
        clear()
        print('PARANG MAY KULANG??')
        time.sleep(7)
        clear()
        print('BYE MUNA:> (run mo nlng ako ulit kapag okay na)')
        time.sleep(7)
        quit()
        
if user_input == 3:
    clear()

    ascii_banner = pyfiglet.figlet_format('BYPASS TOOL')
    print(ascii_banner)

    print('[1]ddosgaurd')
    print('[2]PythoBYPASS')
    print('[3]OVH')
    print('[4]uambypass')

    user_input = int(input('PILI KA PA DITO ISA: '))

    if user_input == 1:
        import subprocess

        cmd = 'node functions.js'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    
    else:
        print('NAGKULANG KA:<')
        time.sleep(5)
        quit()
    
    if user_input == 2:
        from grooming import *
        import subprocess

        cmd = 'python grooming.py'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    else:
        print('NAGKULANG KA:<')
        time.sleep(5)
        quit()

    if user_input == 3:

        import subprocess

        cmd = 'node need.js'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    else:
        print('NAGKULANG KA:<')
        time.sleep(5)
        quit()

    if user_input == 4:
        import subprocess

        cmd = 'node crack.js'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)  

    else:
        print("BULAGA ERROR")
        time.sleep(5)
        quit()

if user_input == 5:
    clear()
    ascii_banner = pyfiglet.figlet_format('DDOSSAMP')
    print(ascii_banner)

    print('[1]SAMPNUDOS')

    user_input = int(input('PILI KA ISA YA: '))

    if user_input == 1:
        from DDOSSAMP.NUDOS import *
        import subprocess
        cmd = 'python NUDOS.py'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    
    else:
        print('BOOM error HAHHAHAHHA')
        quit()

if user_input == 6:
    clear()

    ascii_banner = pyfiglet.figlet_format('403')
    print(ascii_banner)

    print('[1]403bypass')

    user_input = int(input('RAWR: '))

    if user_input == 1:
        from DDOSit import * 
        import subprocess

        cmd = 'bash 403-bypass.sh'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    
    else:
        print('BOOM error HAHHAHAHHA')
        quit()

if user_input == 7:
    clear()

    ascii_banner = pyfiglet.figlet_format('SQLMAP')
    print(ascii_banner)

    print('ganto bai')
    time.sleep(3)
    print('type mo python sqlmap.py -h kung gusto mo ng short ver ng help')
    time.sleep(3)
    print('pag python sqlmap.py -hh namn kapag long ver ha')
    time.sleep(3)
    print('bago mo yan type, type mo muna to cd func')
    time.sleep(3)
    print('un lang bye')
    time.sleep(5)
    print('YOUR ANDROID/COMPUTER SYSTEM WILL BE DELETED IN')
    time.sleep(3)
    print('3')
    time.sleep(2)
    print('2')
    time.sleep(2)
    print('1')
    time.sleep(2)
    print('charot')
    time.sleep(2)
    quit()

if user_input == 8:
    clear()
    
    ascii_banner = pyfiglet.figlet_format('SETOOLKIT')
    print(ascii_banner)

    print('note: you need to install the setup')
    time.sleep(5)

    print('[1]SETUP')
    print('[2]SETOOLKIT')

    user_input = int(input('root@DARKARMY= '))

    if user_input == 1:
        from setoolkit import *
        import subprocess

        cmd = 'python setup.py'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    
    else:
        print('BOOM error HAHHAHAHHA')
        quit()

    if user_input == 2:
        from setoolkit import *
        import subprocess

        cmd = 'setoolkit'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    
    else:
        print('BOOM error HAHHAHAHHA')
        quit()
        