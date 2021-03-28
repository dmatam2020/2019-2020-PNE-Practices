from Client0 import Client
from pathlib import Path
PRACTICE = 2
EXERCISE = 4

print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")
IP = "127.0.0.1"
PORT = 52123
c = Client(IP, PORT)
print(c.talk("Sending the  u5 gene tp the server..."))
print(c.talk(Path("U5.txt").read_text()))