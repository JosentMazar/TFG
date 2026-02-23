import fileinput

def to_ascii(input_ascii):
    
    list_num = input_ascii.split(" ")

    palabra = ""
    for i in  list_num:

        palabra = palabra + chr(int(i)-7)

    return palabra
    
def procesar_linea(linea):
    code = 'OOHKTSJ("'
    pos = 0
    pos = linea.find(code, pos)
    while pos != -1:
        num_asciis = ""
        pos2 = pos + len(code)
        for i in linea[pos2:]:
            
            if i != '"':
                num_asciis = num_asciis + i
            else:
                break
            pos2 = pos2+1
        pos2 = pos2+2
        traduc = to_ascii(num_asciis)
        print(linea[:pos])
        print(traduc)
        print(linea[pos2:])
        linea = linea[:pos] + traduc + linea[pos2:]
        
        pos = linea.find(code, pos + len(traduc))
    return linea    


o = open("keylogger_decod1.txt", "x", encoding="utf-8")

with fileinput.input(files=('a940014a730129f95371c84c982bcbf378586e7afd6eb2f3d0acaf0d15a8ded4 - copia.au3'), encoding="utf-8") as f:
    for line in f:
        linea = procesar_linea(line)
        o.write(linea)

