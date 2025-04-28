import paho.mqtt.client as mqtt
import serial
import time
from datetime import datetime

# Setup serial
ser = serial.Serial('COM3', 9600)  # Change 'COM3' as needed for your Arduino

current_schedule = {"on_time": None, "off_time": None}

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("relay/schedule")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    on_time, off_time = payload.split(",")
    current_schedule["on_time"] = on_time
    current_schedule["off_time"] = off_time
    print(f"Received new schedule: ON at {on_time}, OFF at {off_time}")

def control_light():
    now = datetime.now().strftime("%H:%M")
    if current_schedule["on_time"] and current_schedule["off_time"]:
        if current_schedule["on_time"] <= now < current_schedule["off_time"]:
            ser.write(b'1')
        else:
            ser.write(b'0')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("157.173.101.159", 1883, 60)

client.loop_start()

try:
    while True:
        control_light()
        time.sleep(30)  # check every 30 seconds
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.loop_stop()
    ser.close()
