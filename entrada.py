def LeituraArquivo(NomeArquivo):
    arq = open(NomeArquivo)
    linhas = arq.readlines()
    x = 0
    while x < len(linhas):
        if linhas[x] == "\n":
            local = linhas.index(linhas[x])
            linhas.pop(local)
        else:
            linhas[x] = linhas[x].split(',')
            x += 1

    for i in linhas:
        local = linhas.index(i) 
        for b in i:
            local2 = linhas[local].index(b) 
            if "\n" in b:
                linhas[local][local2] = b.replace("\n",'')
    return linhas