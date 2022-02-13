nBolas = int(input())
linhaDaBola = [int(i) for i in input().split()]


while nBolas > 1:
    proxLinha = []
    for i in range(len(linhaDaBola)-1):
        if linhaDaBola[i] == linhaDaBola[i+1]:
            proxLinha.append(1)
        else:
            proxLinha.append(-1)
    nBolas-= 1
    linhaDaBola = proxLinha

if linhaDaBola[0] == 1:
    print("preta")
else:
    print("branca")