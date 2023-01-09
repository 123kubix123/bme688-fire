import network
import machine
import secrets
import time
try:
    import usocket as socket
except:
    import socket
#import urequests
import bme68x
import json

def blink_onboard_led(num_blinks, delta_t):
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(num_blinks):
        led.on()
        time.sleep(delta_t)
        led.off()
        time.sleep(delta_t)

data = {
    "temperature": 0,
    "pressure": 0,
    "humidity": 0,
    "gas_resistance": 0,
    "air_quality": 0
    }
      

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
blink_onboard_led(5, 0.2)
print("Is wifi connected? {}".format(wlan.isconnected()))

# Create sensor object
sensor = bme68x.BME68X()

url = "https://sirserver.dynovski.xyz/update_data"

while True:
    data = sensor.read_data()
    time.sleep(3)
    
    socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    payload = json.dumps(data)
    request = "POST /update_data HTTP/1.1\r\nHost: raspberry\r\nContent-Length:"+str(len(payload))+" \r\nContent-Type: application/json \r\n\r\n"+payload+"\r\n\r\n"
    print(request)

    address = ("192.168.1.64", 80)
    socketObject.connect(address)
    bytessent = socketObject.send(request)
    socketObject.close()
    print("Socket closed.")
    


