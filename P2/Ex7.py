from Client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")

IP = "192.168.0.241"
PORT = 139
PORT_2 = 25625

c = Client(IP, PORT)
c_2 = Client(IP, PORT_2)


s1 = Seq()
s1.read_fasta("../P2/FRAT1.txt")

count = 0
i = 0
while i < len(s1.strbases) and count < 10:
    fragment = s1.strbases[i:i+10]
    count += 1
    i += 10
    print('Fragment', count, ':', fragment)
    if count % 2 == 0:
        print(c_2.talk('Fragment '+str(count) + ': ' + fragment))
    else:
        print(c.talk('Fragment '+str(count) + ': ' + fragment))