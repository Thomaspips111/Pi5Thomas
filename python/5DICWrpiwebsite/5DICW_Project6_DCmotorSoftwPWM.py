from gpiozero import LED, Button      # Importeer de LED- en Button-klasse
from time import sleep                # Importeer sleep voor vertragingen

motor = LED(20)                        # Definieer GPIO 20 als een motor (LED)
schakelaar = Button(26,pull_up=False)  # Definieer GPIO 26 als een Button (input), interne pull up zetten we af in het object

tijd = 0                              # Variabele voor de duur van de motor

try:
	while True:
		if schakelaar.is_pressed:     # Als de schakelaar wordt ingedrukt
			if tijd < 0.01:           # Verhoog de tijd met 0.001 tot 0.01
				tijd += 0.001
			else:
				tijd = 0.0            # Reset de tijd naar 0.000 als deze 0.01 bereikt
			print(tijd)
			while schakelaar.is_pressed: # Wacht tot de schakelaar wordt losgelaten
				sleep(0.05)           # Vermijd denderen door korte pauze
		motor.on()                    # Zet de motor aan
		sleep(tijd)                   # Houd de motor aan voor de opgegeven tijd
		motor.off()                   # Zet de motor uit
		if tijd < 0.01:               # Voorkom dat de motor uit blijft als de tijd 0 is
			sleep(0.01 - tijd)       # Houd de motor uit voor de rest van de 0.01 seconden
			

except KeyboardInterrupt:
	motor.off()                       # Zet de motor uit
