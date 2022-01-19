digito, número = list(map(int, input().split()))
lista = []
valor = []
valor.append(número)

for i in range(len(valor)):
  if valor[i] != digito:
    lista.append(valor[i])
print(lista)