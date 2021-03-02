import Seq0

ID = "U5.txt"
U5_Seq = Seq0.seq_read_fasta(ID)
dna = U5_Seq[0:20]

base = {"A": "A", "C": "C", "T": "T", "G": "G"}
reverse = "".join([base[b] for b in dna[::-1]])
print("----| Exercise 6 |----")
print("Gene U5:","\nFrag:", dna, "\nRev:", reverse)