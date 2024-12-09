from RPLCD.i2c import CharLCD
import time
# Initialize the LCD using the I2C address of your module
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
			  cols=16, rows=2, dotsize=8, charmap='A02',
			  auto_linebreaks=True, backlight_enabled=True)
while True:
	lcd.write_string("Hello, RPLCD!")
	time.sleep(5)
	lcd.clear()
	lcd.write_string("LCD Test Success!")
	time.sleep(5)

