nPinos , altura = map(int , input().split())

pinos= map(int , input().split())
movimentos=0
#print(pinos)

#for i in range(0,len(pinos),2):
#    while pinos[i]!= altura:
#        for j in range():
#        if pinos[i] < altura:
#            pinos[i]+= pinos[i]
#        if pinos[i] > altura:
#            pinos[i]-= pinos[i]


for i in range(len(pinos)):
    while pinos[i] or pinos[i+1] != altura:
        if pinos[i] == altura:
            pinos[i+1] = pinos[i]
        if pinos[i] and pinos[i+1] != altura:
            movimentos+=movimentos
print(movimentos)
