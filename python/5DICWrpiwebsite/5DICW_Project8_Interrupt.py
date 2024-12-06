from gpiozero import LED, Button      # Importeer de LED- en Button-klasse
from time import sleep                # Importeer sleep voor vertragingen

# Definieer de LED's op de respectievelijke GPIO-pinnen
rode_led = LED(16)                    
groene_led = LED(20)                  
blauwe_led = LED(21)                  

# Definieer de drukknop op GPIO 5
drukknop = Button(5, bounce_time=0.3)  # Bounce time ingesteld op 300ms

# Functie die wordt aangeroepen wanneer de drukknop wordt ingedrukt
def drukknop_ingevoegd():
    rode_led.on()                     # Zet alle LED's aan (wit licht)
    groene_led.on()
    blauwe_led.on()

# Koppel de drukknop aan de functie met 'when_pressed'
drukknop.when_pressed = drukknop_ingevoegd

try:
    while True:
        rode_led.on()                 # Zet alleen de rode LED aan
        groene_led.off()
        blauwe_led.off()
        sleep(1)                      # Wacht 1 seconde

        rode_led.off()                # Zet alleen de groene LED aan
        groene_led.on()
        blauwe_led.off()
        sleep(1)                      # Wacht 1 seconde

        rode_led.off()                # Zet alleen de blauwe LED aan
        groene_led.off()
        blauwe_led.on()
        sleep(1)                      # Wacht 1 seconde

except KeyboardInterrupt:
    rode_led.off()                    # Zet alle LED's uit bij afsluiten
    groene_led.off()
    blauwe_led.off()
