from gpiozero import Motor           # Importeer de Motor-klasse
from time import sleep               # Importeer sleep voor vertragingen
import sys                           # Importeer sys voor afsluiten

# Definieer de motor met pinnen 22 en 21 als de 'forward' en 'backward' aansluitingen
motor = Motor(forward=22, backward=21)

try:
    while True:
        motor.forward()              # Motor linksom draaien (forward)
        sleep(1)                     # Draai 1 seconde
        motor.backward()             # Motor rechtsom draaien (backward)
        sleep(1)                     # Draai 1 seconde

except KeyboardInterrupt:            # Als "ctrl+c" wordt gedrukt
    motor.stop()                     # Motor stilleggen
    sys.exit()                       # Programma afsluiten
