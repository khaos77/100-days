def romanToInt(s):
        tabela = {
            'I':  1,
            'V':  5,
            'X':  10,
            'L':  50,
            'C':  100,
            'D':  500,
            'M':  1000
        }
        cont = 0 
        for i in range(len(s) -1):
            if tabela[s[i]] < tabela[s[i+1]]:
                cont -= tabela[s[i]]
            else:
                cont += tabela[s[i]]
        return cont + tabela[s[-1]]

a = romanToInt('MCMXIV')
print(a)