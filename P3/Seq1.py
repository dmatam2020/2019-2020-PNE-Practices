import termcolor
from pathlib import Path

class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = 'NULL'
    INVALID_SEQUENCE = 'ERROR'

    def __init__(self, strbases=NULL_SEQUENCE):
        self.strbases = strbases

        if strbases == Seq.NULL_SEQUENCE:
            print('NULL Seq created')
            self.strbases = strbases

        else:
            if self.is_valid_sequence():
                self.strbases = strbases
                print('New sequence created!')

            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print('INVALID Seq!')

    def is_valid_sequence(self):

        for i in self.strbases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False

        return True

    @staticmethod
    def is_valid_sequence_2(bases):

        for i in strbases:

            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False

        return True
    @staticmethod

    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            #in order to use termcolor, we need to pass the first argument(text) as a whole string, the second argument would be the color we want to use
            text = 'Sequence' + str(i) + ': (Length:' + str(list_sequences[i].len()) + ')'+ str(list_sequences[i])
            termcolor.cprint(text, 'yellow')

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if not (self.strbases == Seq.NULL_SEQUENCE) and not(self.strbases == Seq.INVALID_SEQUENCE):
            for i in self.strbases:
                if i == 'A':
                    a += 1
                elif i == 'C':
                    c += 1
                elif i == 'G':
                    g += 1
                else:
                    t += 1
        return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {'A': a, 'C': c, 'G': g, 'T': t}

    def count_genes_info(self):
        a, c, g, t = self.count_bases()
        total_sum = a + c + g + t
        pa = a * 100 / total_sum
        pc = c * 100 / total_sum
        pg = g * 100 / total_sum
        pt = t * 100 / total_sum
        return {'A': [a, pa], 'C': [c, pc], 'G': [g, pg], 'T': [t, pt]}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'NULL'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'ERROR'
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            complement = ''
            for i in self.strbases:
                if i == 'A':
                    complement += 'T'
                elif i == 'C':
                    complement += 'G'
                elif i == 'G':
                    complement += 'C'
                elif i == 'T':
                    complement += 'A'
            return complement
    @staticmethod


    def take_out_first_line(sequence):
        return sequence[sequence.find("\n") + 1:].replace("\n","")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())

    def most_common_base(dictionary):
        most_common = max(dictionary.values())
        for k, v in dictionary.items():
            if v == most_common:
                return k

def test_sequences():
    s1 = Seq()
    s2 = Seq('ACTGA')
    s3 = Seq('Invalid Sequence')
    return s1, s2, s3