from Client0 import Client
PRACTICE = 2
EXERCISE = 1

print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")
IP ="192.168.0.241"
PORT = 139
c = Client(IP, PORT)
c.ping()
print(f"IP: {c.ip}, {c.port}")