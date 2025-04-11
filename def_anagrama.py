def anagrama(lista):
    if not lista:
        return None, 0
    
    lista_palavras = []
    for palavra1, palavra2 in lista:
        dicionario1 =  {}
        for letra in dicionario1:
            if letra in dicionario1:
                dicionario1[letra] += 1
            else:
                dicionario1[letra] = 1
        dicionario2 =  {}
        for letra in dicionario2:
            if letra in dicionario2:
                dicionario2[letra] += 1
            else:
                dicionario2[letra] = 1
        if dicionario1 == dicionario2:
            lista_palavras = lista_palavras + [True]
        else:
            lista_palavras = lista_palavras + [False]
    return lista_palavras

lista = [('amor', 'roma'), ('python', 'nothyp'), ('casa', 'saco')]
resultado = anagrama(lista)
print(resultado)
