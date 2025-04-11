def reverter_palavras(lista):
    if not lista:
        return None, 0

    palavras_invertidas = []
    for i in lista:
        palavras_invertidas = palavras_invertidas + [i[::-1]]

    return palavras_invertidas

lista_palavras = ['CPU', 'Kernel']
print(reverter_palavras(lista_palavras))