from Seq1 import Seq, test_sequences

def print_result(i, sequence):
    print('Sequence ' + str(i) + ': (Length: ' + str(sequence.len()) + ') ' + str(sequence))
    print('Bases: ', sequence.count())

print('-----|Practice 1, Exercise 6|-----')
list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])