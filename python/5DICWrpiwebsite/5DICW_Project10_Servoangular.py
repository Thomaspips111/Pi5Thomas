from gpiozero import AngularServo
from time import sleep

# Maak een AngularServo-object aan. Pas de pin aan naar waar je servo is aangesloten.
# Hier gebruiken we GPIO 21 als voorbeeld.
servo = AngularServo(21, initial_angle=0, min_angle=0, max_angle=180, min_pulse_width=7/10000, max_pulse_width=25/10000)
#min_pulse_width=7/10000, max_pulse_width=25/10000) ==> hangt van servo tot servo af

try:
    while True:
        # Servo naar 0 graden draaien
        print("Draai naar 0 graden")
        servo.angle = 0
        sleep(2)
        
        # Servo naar 90 graden draaien
        print("Draai naar 90 graden")
        servo.angle = 90
        sleep(2)
        
        # Servo naar -90 graden draaien
        print("Draai naar -90 graden")
        servo.angle = 180
        sleep(2)

except KeyboardInterrupt:
    # Stop het programma netjes als je op Ctrl+C drukt
    print("Programma beëindigd")

