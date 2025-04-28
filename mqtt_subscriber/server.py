import asyncio
import websockets
import json
import subprocess

MQTT_BROKER = '157.173.101.159'
MQTT_PORT = '1883'
MQTT_TOPIC = 'relay/schedule'

async def handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        on_time = data["on_time"]
        off_time = data["off_time"]

        mqtt_message = f"{on_time},{off_time}"
        # Publish to MQTT using mosquitto_pub
        subprocess.run([
            "mosquitto_pub",
            "-h", MQTT_BROKER,
            "-p", MQTT_PORT,
            "-t", MQTT_TOPIC,
            "-m", mqtt_message
        ])

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
