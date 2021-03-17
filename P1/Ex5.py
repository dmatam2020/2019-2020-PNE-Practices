from Seq1 import Seq

def print_result(i, sequence):
    print('Sequence ' + str(i) + ': (Length: ' + str(sequence.len()) + ') ' + str(sequence))
    a, c, t, g= sequence.count_bases()
    print('A: ' + str(a) + ', C: ' + str(c) + ', T: ' + str(t) + ', G: '+ str(g))
print('-----|Practice 1, Exercise 5|-----')
s0 = Seq()
s1 = Seq('ACTGA')
s2 = Seq('Invalid Sequence')

list_seq = [s0, s1, s2]
for i in range(0, 3):
    print_result(i, list_seq[i])