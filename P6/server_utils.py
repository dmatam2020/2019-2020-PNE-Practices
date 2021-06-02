import Seq1 as Seq
import jinja2
import pathlib

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print("To server: ", end="")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def ping(cs):
    print_colored("PING", "green")
    response = "OK!"
    cs.send(str(response).encode())
    print(response)

def get(list_sequences, seq_number):
    sequence = list_sequences[int(seq_number)]
    context = {
        "number": seq_number,
        "sequence": sequence
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents

def info(sequence):
    sequence = Seq.Seq(sequence)
    response = "\nTotal length: " + str(sequence.len())
    list_letters = ["A", "C", "G", "T"]
    sol = " "
    for i in range(0, 4):
        sol += "<br><br>" + list_letters[i] + ":" + str(sequence.count_bases()[i]) + " (" + str(sequence.percentage()[i]) + "%)"
        i += 1
    ans = response + sol

    context = {
        "sequence": sequence,
        "operation": "info",
        "result": ans
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def comp(sequence):
    sequence = Seq.Seq(sequence)
    response = sequence.complement()
    context = {
        "sequence": sequence,
        "operation": "comp",
        "result": response
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def rev(sequence):
    sequence = Seq.Seq(sequence)
    response = sequence.reverse()
    context = {
        "sequence": sequence,
        "operation": "rev",
        "result": response
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def gene(seq_name):
    PATH = "./Sequences/" + seq_name + ".txt"
    s1 = Seq.Seq()
    s1.read_fasta(PATH)
    context = {
        "gene_name": seq_name,
        "gene_contents": s1.strbases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents