from Client0 import Client
from pathlib import Path
PRACTICE = 2
EXERCISE = 4

print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")
IP = "192.168.0.241"
PORT = 139
c = Client(IP, PORT)
print(c.talk("Sending the  U5 gene to the server..."))
print(c.talk(Path("U5.txt").read_text()))