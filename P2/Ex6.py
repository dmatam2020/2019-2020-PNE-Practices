from Client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")
IP = "127.0.0.1"
PORT = 52123
c = Client(IP, PORT)


s1 = Seq()
s1.read_fasta("../Session 4/FRAT1")

count = 0
i = 0
while i < len(s1.strbases) and count < 5:
    fragment = s1.strbases[i:i+10]
    count += 1
    i += 10
    print('Fragment', count, ':', fragment)
    print(c.talk(fragment))