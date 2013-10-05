def invertida(palavra):
    return palavra[::-1]

lista = sorted(frutas, key=invertida)

lista = sorted(frutas, key=lambda s: s[::-1])
