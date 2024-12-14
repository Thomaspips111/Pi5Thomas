import serial
import time

# Setup serial connection (adjust the port as needed, often /dev/ttyAMA0 for the Pi)
bluetooth_port = '/dev/serial0'  # For Raspberry Pi
baud_rate = 115000  # Baud rate for HC-05 module

# Initialize serial connection
ser = serial.Serial(bluetooth_port, baud_rate)

# Function to send data to HC-05
def send_data(data):
	ser.write(data.encode())  # send data to HC-05 module
	print(f"Sent: {data}")

# Function to receive data from HC-05
def receive_data():
	if ser.in_waiting > 0:  # If there is incoming data from HC-05
		data = ser.readline().decode('utf-8').strip()  # Read and decode the data
		return data
	return None

try:
	# Keep the connection alive and send/receive data
	while True:
		send_data("Hello from Raspberry Pi!")
		time.sleep(2)  # Wait for 2 seconds before sending another message
		
		received = receive_data()
		if received:
			print(f"Received: {received}")
		
		time.sleep(1)  # Wait for 1 second before checking again

except KeyboardInterrupt:
	print("\nProgram interrupted.")
finally:
	ser.close()  # Close the serial connection
	print("Serial connection closed.")
