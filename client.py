import requests
import base64

with open("data", "r") as f:
    data = f.read().rstrip('\n')

data = []
for i in range(100):
    data += [base64.b64encode(bytearray([int(i/10), 0, 0] * 144))]

def fade_in():
    for i in range(100):
        requests.post("http://localhost:8080/api/render", data=data[i])

def fade_out():
    for i in range(100):
        requests.post("http://localhost:8080/api/render", data=data[99-i])

for i in range(10):
    fade_in()
    fade_out()

requests.get("http://localhost:8080/api/clear")
