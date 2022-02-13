nPinos , altura = list(map(int, input().split()))

pinos= list(map(int, input().split()))
movimentos=0
#print(pinos)

for i in range(nPinos):
    while pinos[i]!= altura:
        if pinos[i] < altura:
            pinos[i]= pinos[i]+1
            pinos[i+1]=pinos[i+1]+1
            movimentos=movimentos+1
            
        if pinos[i] > altura:
            pinos[i]= pinos[i]-1
            pinos[i+1]=pinos[i+1]-1
            movimentos=movimentos+1
print(movimentos) 