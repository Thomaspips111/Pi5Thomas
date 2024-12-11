import serial
import os
import threading                      # Importeer de threading-module
import sys

serialport = serial.Serial('/dev/serial0', 9600, timeout=0.5)

def lees_signaal():
    while True:
        response = serialport.read(20)
        if response:
            print("\n!Binnenkomend signaal!\n----------------------")
            sing = response.decode('utf-8')
            print(sing+'\n')
            print("Invoer: ")

os.system('clear')
# Start een nieuwe thread voor de led1_blink functie
led1_thread = threading.Thread(target=lees_signaal)
led1_thread.daemon = True         # Maakt de thread daemon, thread stopt als hoofdprogramma stopt
led1_thread.start()               # Start de thread
try :
    while True:
        serialcmd = input("Invoer:\n")
        for _ in range(len(serialcmd)+1):
            print("-", end='')
        print()
        serialport.write((serialcmd).encode('utf-8'))
except KeyboardInterrupt:
    os.system('clear')
    serialport.close()
    sys.exit()