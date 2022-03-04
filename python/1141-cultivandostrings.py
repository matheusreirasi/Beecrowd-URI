def sequenciaFotos():
        for i in range(len(strings)):
            if len(strings[i]) > len(strings[i+1]):
                for j in strings:
                    if strings[i] == strings[j]:
                        

fotos = int(input())
strings = []

for i in range(fotos):
    strings[i] = input()

while fotos != 0:
    sequenciaFotos(strings)
print(maiorSequencia)## ainda não criei maior sequência