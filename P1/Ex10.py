from Seq1 import Seq
print('-----|Practice 1, Exercise 10|-----')
GENE_FOLDER = "./Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in gene_list:
    s1 = Seq()
    sequence = Seq.read_fasta(Seq, GENE_FOLDER + gene + ".txt")
    print("Gene", gene,": Most frequent base:", (Seq.most_common_base(Seq.count_genes(Seq))))
