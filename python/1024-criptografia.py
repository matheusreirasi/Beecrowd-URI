from math import ceil


def criptografia (lista):
    #Passo 1
    for i in range(len(lista)):
        if lista[i].isalpha():
            lista[i] = chr(ord(lista[i])+3)
    #Passo 2
    for i in range(len(lista)):
        lista[i] = lista[i][::-1]
    #Passo 3
    for i in range(len(lista)):
        lista[i] = ceil(len(lista[i]/2))
        lista[i] = chr(ord(lista[i]-1))
        
casos = int(input())
lista = []
for i in range(casos):
    lista.append(input())

criptografia(lista)
