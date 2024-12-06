from gpiozero import LED                # Importeer de benodigde klasse
from time import sleep                  # Vereenvoudig "time.sleep()" naar "sleep()"

led = LED(22)                           # Definieer GPIO 10 als een LED (OUTPUT)

try:
    while True:
        led.on()                        # Zet de LED aan (stuur HOOG naar GPIO 10)
        sleep(0.1)                      # Wacht 100ms
        led.off()                       # Zet de LED uit (stuur LAAG naar GPIO 10)
        sleep(0.1)                      # Wacht 100ms

except KeyboardInterrupt:               # Als "ctrl+c" wordt getoetst
    led.off()                           # Zet de LED uit
