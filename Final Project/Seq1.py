import pathlib

class Seq:
    NULL ='NULL'
    INVALID ='ERROR'

    def __init__(self, strbases=NULL):
        if strbases == Seq.NULL:
            print("NULL Seq Created")
            self.strbases = strbases
        elif Seq.is_valid_sequence_2(strbases):
            self.strbases=strbases
            print('New sequence created')
        else:
            self.strbases=Seq.INVALID
            print('Invalid sequence')



    @staticmethod
    def is_valid_sequence_2(strbases):
        for c in strbases:
            if c!='A' and c !='C' and c!='G' and c!= 'T':
               return False
        return True

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == Seq.NULL or self.strbases==Seq.INVALID:
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        bases = ["A", "C", "T", "G"]
        count_bases = []
        for base in bases:
            count_bases.append(self.count_base(base))
        dictionary = dict(zip(bases, count_bases))
        return dictionary

    def percentage(self):
        list_bases = ["A", "C", "T", "G"]
        list_percentages = []
        total = len(self.strbases)
        for base in list_bases:
            percentage = self.count_base(base) * 100 / total
            list_percentages.append(percentage)
        return list_percentages

    @staticmethod
    def reverse(seq_rev):
        rev_seq = ''
        for e in seq_rev[::-1]:
          rev_seq += e
        return rev_seq
    @staticmethod
    def complement(seq_comp):
        BLANK = ''
        for e in seq_comp:
            if e == "A":
                BLANK += "T"
            if e == "T":
                BLANK += "A"
            if e == "C":
                BLANK += "G"
            if e == "G":
                BLANK += "C"
        return BLANK

    @staticmethod
    def read_fasta(filename):
            file_lines = pathlib.Path('../P3/' + str(filename) + '.txt').read_text().split("\n")
            body = (file_lines[1:])
            strbases = ''.join(body)
            return strbases