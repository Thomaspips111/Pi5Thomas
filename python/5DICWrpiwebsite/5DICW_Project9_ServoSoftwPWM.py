from gpiozero import PWMOutputDevice  	# Importeer de PWMOutputDevice-klasse
from time import sleep                  # Importeer sleep voor vertragingen
import sys                              # Importeer sys voor afsluiten

# Definieer de PWM-output op GPIO 21 met een frequentie van 50Hz
servo = PWMOutputDevice(21, frequency=50, initial_value=0)

teller = 0.00                          # Teller moet kommagetal zijn zodat DCservo een float wordt

try:
    while True:
        if teller < 100:                # Teller optellen: 0 = 0 graden, 100 = 180 graden
            teller += 10

        if teller == 100:
            teller = 0.00

        DCservo = 3.75 + ((teller / 100) * 7.5)  # Berekening voor duty cycle
        print("DutyCycle servo: " + str(DCservo))

        servo.value = DCservo / 100      # Zet de waarde voor de PWM-output (0-1)
        sleep(0.5)

except KeyboardInterrupt:
    servo.value = 0                      # Stop de PWM door de waarde op 0 te zetten
    sys.exit()                           # Programma afsluiten
