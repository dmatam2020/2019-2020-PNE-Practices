from pathlib import Path


def seq_ping():
    print("OK.")


def take_out_first_line(seq):
    return seq[seq.find('\n') + 1:].replace('\n', '')


def seq_read_fasta(filename):
    return take_out_first_line(Path(filename).read_text())


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    return seq.count(base)


def seq_count(seq):
    a, c, g, t = 0, 0, 0, 0
    for d in seq:
        if d == "A":
            a += 1
        elif d == "C":
            c += 1
        elif d == "G":
            g += 1
        else:
            t += 1
    return {"A": a, "C": c, "G": g, "T": t}


def seq_reverse(seq):
    reverse = ""
    for base in seq:
        reverse = base + reverse
    return reverse


def seq_complement(seq):
    return seq_complement(seq)


def most_common_base(dictionary):
    most_common = max(dictionary.values())
    for k, v in dictionary.items():
        if v == most_common:
            return k