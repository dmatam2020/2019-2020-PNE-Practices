from Client0 import Client
from pathlib import Path
from Seq1 import Seq
import colorama

PRACTICE = 2
EXERCISE = 4

print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")
IP = "192.168.0.241"
PORT = 139
c = Client(IP, PORT)

print(c)

c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")