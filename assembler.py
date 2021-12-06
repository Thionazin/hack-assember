import sys

line_counter = 0
counter = 16
glob_dic = {}

def handle_dest(seg):
    if seg == 'M':
        return '001'
    if seg == 'D':
        return '010'
    if seg == 'MD':
        return '011'
    if seg == 'A':
        return '100'
    if seg == 'AM':
        return '101'
    if seg == 'AD':
        return '110'
    if seg == 'AMD':
        return '111'

def handle_comp(seg):
    if seg == '0':
        return '0101010'
    if seg == '1':
        return '0111111'
    if seg == '-1':
        return '0111010'
    if seg == 'D':
        return '0001100'
    if seg == 'A':
        return '0110000'
    if seg == '!D':
        return '0001101'
    if seg == '!A':
        return '0110001'
    if seg == '-D':
        return '0001111'
    if seg == '-A':
        return '0110011'
    if seg == 'D+1':
        return '0011111'
    if seg == 'A+1':
        return '0110111'
    if seg == 'D-1':
        return '0001110'
    if seg == 'A-1':
        return '0110010'
    if seg == 'D+A' or 'A+D':
        return '0000010'
    if seg == 'D-A':
        return '0010011'
    if seg == 'A-D':
        return '0000111'
    if seg == 'D&A' or seg == 'A&D':
        return '0000000'
    if seg == 'D|A' or seg == 'A|D':
        return '0010101'
    if seg == 'M':
        return '1110000'
    if seg == '!M':
        return '1110001'
    if seg == '-M':
        return '1110011'
    if seg == 'M+1':
        return '1110111'
    if seg == 'M-1':
        return '1110010'
    if seg == 'D+M' or seg == 'M+D':
        return '1000010'
    if seg == 'D-M':
        return '1010011'
    if seg == 'M-D':
        return '1000111'
    if seg == 'D&M' or seg == 'M&D':
        return '1000000'
    if seg == 'D|M' or seg == 'M|D':
        return '1010101'
    


def handle_jump(seg):
    if seg == 'JGT':
        return '001'
    if seg == 'JEQ':
        return '010'
    if seg == 'JGE':
        return '011'
    if seg == 'JLT':
        return '100'
    if seg == 'JNE':
        return '101'
    if seg == 'JLE':
        return '110'
    if seg == 'JMP':
        return '111'



def handle_c(line):
    dest = ""
    comp = ""
    jump = ""
    first_cut = line.split(';')
    second_cut = first_cut[0].split('=')
    if len(first_cut) != 1:
        jump = handle_jump(first_cut[1].strip())
    else:
        jump = "000"
    if len(second_cut) == 2:
        dest = handle_dest(second_cut[0].strip())
        comp = handle_comp(second_cut[1].strip())
    else:
        dest = "000"
        comp = handle_comp(second_cut[0].strip())
    output_string = "111" + comp + dest + jump
    return output_string


def handle_a(line):
    line=line.strip("\n")
    if line[1:] == 'SP':
        return '0000000000000000'
    elif line[1:] == 'LCL':
        return '0000000000000001'
    elif line[1:] == 'ARG':
        return '0000000000000010'
    elif line[1:] == 'THIS':
        return "{0:b}".format(3).zfill(16)
    elif line[1:] == 'THAT':
        return "{0:b}".format(4).zfill(16)
    elif line[1:] == 'R0':
        return "{0:b}".format(0).zfill(16)
    elif line[1:] == 'R1':
        return "{0:b}".format(1).zfill(16)
    elif line[1:] == 'R2':
        return "{0:b}".format(2).zfill(16)
    elif line[1:] == 'R3':
        return "{0:b}".format(3).zfill(16)
    elif line[1:] == 'R4':
        return "{0:b}".format(4).zfill(16)
    elif line[1:] == 'R5':
        return "{0:b}".format(5).zfill(16)
    elif line[1:] == 'R6':
        return "{0:b}".format(6).zfill(16)
    elif line[1:] == 'R7':
        return "{0:b}".format(7).zfill(16)
    elif line[1:] == 'R8':
        return "{0:b}".format(8).zfill(16)
    elif line[1:] == 'R9':
        return "{0:b}".format(9).zfill(16)
    elif line[1:] == 'R10':
        return "{0:b}".format(10).zfill(16)
    elif line[1:] == 'R11':
        return "{0:b}".format(11).zfill(16)
    elif line[1:] == 'R12':
        return "{0:b}".format(12).zfill(16)
    elif line[1:] == 'R13':
        return "{0:b}".format(13).zfill(16)
    elif line[1:] == 'R14':
        return "{0:b}".format(14).zfill(16)
    elif line[1:] == 'R15':
        return "{0:b}".format(15).zfill(16)
    elif line[1:] == 'SCREEN':
        return "{0:b}".format(16384).zfill(16)
    elif line[1:] == 'KBD':
        return "{0:b}".format(24576).zfill(16)
    elif line[1:] in glob_dic:
        return "{0:b}".format(glob_dic[line[1:]]).zfill(16)
    elif line[1:].isnumeric():
        return "{0:b}".format(int(line[1:])).zfill(16)
    else:
        global counter
        glob_dic[line[1:]] = counter
        counter += 1
        return "{0:b}".format(glob_dic[line[1:]]).zfill(16)


def handle_l(line):
    line = line.strip()
    line = line.strip("()")
    global line_counter
    print(line)
    glob_dic[line] = line_counter


def main():
    global line_counter
    inputfile = open(sys.argv[1], 'r')
    temporary = sys.argv[1].split(".")
    output = open(temporary[0]+'.hack', 'w')
    outputs = []
    file_read = inputfile.readlines()
    for line in file_read:
        if line[0] == '@':
            outputs.append(handle_a(line) + "\n")
            line_counter += 1
        elif line[0] == '(':
            handle_l(line)
        else:
            outputs.append(handle_c(line) + "\n")
            line_counter += 1
    output.writelines(outputs)

if __name__ == "__main__":
    main()
