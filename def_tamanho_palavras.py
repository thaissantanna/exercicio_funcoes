def maior_palavra(lista):
    if not lista:
        return None, 0
    max_palavra = max(lista, key=len)
    return max_palavra, len(max_palavra)

def menor_palavra(lista):
    if not lista:
        return None, 0
    min_palavra = min(lista, key=len)
    return min_palavra, len(min_palavra)


lista_palavras = ['CPU', 'Kernel', 'Programação','inconstitucionalissimamente']

print(maior_palavra(lista_palavras))
print(menor_palavra(lista_palavras))