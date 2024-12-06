from gpiozero import LED              # Importeer de LED-klasse
from time import sleep                # Importeer sleep voor vertragingen
import threading                      # Importeer de threading-module

# Definieer de LED's op de respectievelijke GPIO-pinnen
led1 = LED(5)                         
led2 = LED(6)                         

def led1_blink():
    while True:                       # LED1 flikkert continu in een aparte thread
        led1.on()
        sleep(0.2)
        led1.off()
        sleep(0.2)

try:
    # Start een nieuwe thread voor de led1_blink functie
    led1_thread = threading.Thread(target=led1_blink)
    led1_thread.daemon = True         # Maakt de thread daemon, thread stopt als hoofdprogramma stopt
    led1_thread.start()               # Start de thread

    while True:
        led2.on()                     # LED2 flikkert in de hoofdthread
        sleep(1)
        led2.off()
        sleep(1)

except KeyboardInterrupt:
    led1.off()                        # Zet alle LED's uit bij afsluiten
    led2.off()
