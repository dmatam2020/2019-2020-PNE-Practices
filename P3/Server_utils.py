
def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")  # for pycharm's console to return colors and not weird symbols
    print(termcolor.colored("Message", "yellow"))
def format_command(command):
    return command.replace("\n", "").replace("\r","")
def ping():
    print_colored("PING command!", "green")
    response = "OK!"
    cs.send(str(response).encode())

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())
def info(cs, argument):
    termcolor.cprint('INFO', 'green')
    s = Seq(argument)
    info_dict = s.info_seq()
    response1 = 'Total length: ' + str(len(argument)) + '\n'
    cs.send(response1.encode())
    response2 = 'A: ' + str(info_dict['A'][0]) + ' ' + str(info_dict['A'][1]) + '%' + '\n'
    cs.send(response2.encode())
    response3 = 'C: ' + str(info_dict['C'][0]) + ' ' + str(info_dict['C'][1]) + '%' + '\n'
    cs.send(response3.encode())
    response4 = 'G: ' + str(info_dict['G'][0]) + ' ' + str(info_dict['G'][1]) + '%' + '\n'
    cs.send(response4.encode())
    response5 = 'T: ' + str(info_dict['T'][0]) + ' ' + str(info_dict['T'][1]) + '%' + '\n'
    cs.send(response5.encode())
    print(response1, response2, response3, response4, response5)

def comp(cs, argument):
    termcolor.cprint('COMP', 'green')
    s = Seq(argument)
    complement = s.complement()
    response = complement + '\n'
    cs.send(response.encode())
    print(response)

def rev(cs, argument):
    termcolor.cprint('REV', 'green')
    s= Seq(argument)
    rev = s.reverse()
    response = rev + '\n'
    cs.send(response.encode())
    print(response)

def gene(cs, argument):
    gene_loc = './sequences/'
    termcolor.cprint('GENE', 'green')
    s = Seq()
    s.read_fasta(gene_loc + argument)
    response = str(s) + '\n'
    print(response)
    cs.send(response.encode())