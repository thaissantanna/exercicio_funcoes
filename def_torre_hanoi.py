class Torre:
    def __init__(self, nome):
        self.nome = nome
        self.pilha = []

    def push(self, disco):
        if self.pilha and self.pilha[-1] < disco:
            raise ValueError("Não é permitido colocar disco maior sobre um menor.")
        self.pilha.append(disco)

    def pop(self):
        if not self.pilha:
            raise IndexError("Tentativa de remover disco de torre vazia.")
        return self.pilha.pop()

    def __str__(self):
        return f"{self.nome}: {self.pilha}"


def mover_discos(n, origem, destino, auxiliar):
    if n == 1:
        disco = origem.pop()
        destino.push(disco)
        print(f"Move disco {disco} de {origem.nome} para {destino.nome}")
    else:
        mover_discos(n-1, origem, auxiliar, destino)
        mover_discos(1, origem, destino, auxiliar)
        mover_discos(n-1, auxiliar, destino, origem)


# Inicializando torres
n_discos = 5
origem = Torre("Origem")
destino = Torre("Destino")
auxiliar = Torre("Auxiliar")

# Colocando discos na torre de origem
for disco in range(n_discos, 0, -1):
    origem.push(disco)

# Resolvendo o problema
mover_discos(n_discos, origem, destino, auxiliar)

# Exibindo o estado final das torres
print(origem)
print(destino)
print(auxiliar)