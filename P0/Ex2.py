import Seq0

ID = "U5.txt"

U5_Seq = Seq0.seq_read_fasta(ID)
print("DNA file:", ID)
print("The first 20 bases are:\n",U5_Seq[0:20])

