from gpiozero import Button           # Importeer de Button-klasse voor GPIO input
from time import sleep                # Vereenvoudig "time.sleep()" naar "sleep()"
import sys                            # sys library importeren

button = Button(26,pull_up=False)     # Definieer GPIO 21 als een Button (input), interne pull up zetten we af in het object


try:
    teller = 0                        # Nieuwe variabel "teller" aanmaken

    while True:
        if button.is_pressed:         # ALS GPIO 21 een input krijgt DAN:
            teller += 1               # teller telt op
            if teller > 10:           # als de teller boven 10 komt,
                teller = 0            # reset de teller naar 0
            print(teller)             # teller op uitvoer zetten

        while button.is_pressed:      
            pass                      # Doe niets totdat knop wordt losgelaten
        sleep(0.05)                   # Wacht 50ms om dender te vermijden

except KeyboardInterrupt:             # Als "ctrl+c" wordt gedrukt
    sys.exit()                        # Alles resetten zodat we alles afsluiten
