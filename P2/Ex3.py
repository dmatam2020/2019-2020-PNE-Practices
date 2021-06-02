from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")
IP = "192.168.0.241"
PORT = 139
c = Client(IP, PORT)
print("response: ", c.talk('This is something random'))
