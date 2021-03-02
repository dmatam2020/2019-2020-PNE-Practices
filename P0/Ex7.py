import Seq0

ID = "U5.txt"

U5_Seq = Seq0.seq_read_fasta(ID)
complement = {"A": "T", "C": "G", "T": "A", "G": "C"}

original = U5_Seq[0:20]
cmp = "".join(complement[letter] for letter in original)

print("-----| Exercise 7 |-----")
print("The complement is: {}".format(cmp))