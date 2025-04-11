def palindromo(lista):
    if not lista:
        return None, 0

    lista_palavras = []
    for i in lista:
        if i == i[::-1]:
            lista_palavras = lista_palavras + [True]
        else:
            lista_palavras = lista_palavras + [False]

    return lista_palavras

print(palindromo(["ovo", "python", "radar"]))