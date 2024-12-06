from gpiozero import RGBLED
import atexit #Om een functie te doorlopen wanneer de server afsluit
from flask import Flask, render_template, request
import threading
from time import sleep

# Initialiseer de RGB LED (rood, groen, blauw)
rgb_led = RGBLED(red=19, green=26, blue=13)

teller = 0
telleroud = 0
aanuit = 1

#Het ip adres wordt statisch verkregen
#De template folder (default templates, meestal gebruikt voor html enzo) veranderen we in www
#De static folder (default static, meestal gebruikt voor CSS enzo) veranderen we in www
app = Flask(__name__, static_url_path='', static_folder='www', template_folder='www')
#Als de host (ip van je raspberry pi) opgevraagd wordt op de root directory ('/') 
#dan gaan we de functie "index" uitvoeren
#functie "index"

def main():
	global aanuit
	print("test")
	while True:
		if aanuit == 0:
			rgb_led.color = (1, 0, 0)  # Rood
		print("rood")
		if aanuit == 1:
			rgb_led.color = (0, 0, 0)  # Groen
		sleep(1)

#main programma in multithread
main_thread = threading.Thread(target=main, daemon=True)
main_thread.start()

@app.route('/')
def index():
	#webpagina laden
	return render_template('index.html')

@app.route('/led',methods=["POST"])
def led():
	global aanuit
	#aanuit moet veranderd worden voor return, dus is 1 uit en 0 aan
	if aanuit == 1:
		aanuit = 0 
		return "LED is aan"
		
	elif aanuit == 0:
		aanuit = 1
		return "LED is uit"		

@app.route('/tijd')
def tijd():
	global teller
	global telleroud
	global aanuit
	while aanuit == 0:
		teller += 1
		telleroud = teller
		return "LED is al " + str(teller) + " seconden aan."
	if aanuit == 1:
		teller = 0
		return "LED was " + str(telleroud) + " seconden aan."

def stop():
	rgb_led.off()

if __name__ == '__main__':
#host='0.0.0.0' ==> De webapp is nu toegankelijk via het ip van de raspberry pi. 
#De webapp gaat luisteren op poort 5050
	#functie 'stop' doorlopen wanneer server stopt
	atexit.register(stop)
	app.run(debug=True, host='0.0.0.0',port=5050, use_reloader=False)
