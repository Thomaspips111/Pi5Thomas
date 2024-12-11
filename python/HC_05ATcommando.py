import serial
import os
import threading                      # Importeer de threading-module
serialport = serial.Serial('/dev/serial0', 9600, timeout=0.5)

def safe_exit(signum, frame):
    exit(1)


def lezen():
	while True:
		response = serialport.read(20)
		if response:
			test = response.decode('utf-8')
			print(test)
			print("eee")

os.system('clear')
# Start een nieuwe thread voor de led1_blink functie
led1_thread = threading.Thread(target=lezen)
led1_thread.daemon = True         # Maakt de thread daemon, thread stopt als hoofdprogramma stopt
led1_thread.start()               # Start de thread
try : 
	baud = int(input('ATmode (38400) normalmode (9600)'))
	serialport = serial.Serial('/dev/serial0', baud, timeout=0.5)
	while True:
		serialcmd = input("serial command: ")
		serialport.write ((serialcmd + '\r\n').encode('utf-8'))
except KeyboardInterrupt:
	os.system('clear')