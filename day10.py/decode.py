#codifica senha dada pelo usuario
def codepass(senha):
    string = ''
    normal = "abcdefghijklmnopqrstuvwxyz"
    coded = "@B$&3fg419K|mn0#qR(*-,=+~?"

    for i in senha:
        if i in normal:
            pos = normal.find(i)
            string += coded[pos]

    return string






senha = input().split()
print(codepass(senha[0]))