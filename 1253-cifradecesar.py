casos = int(input())

for i in range(casos):
    texto = input()
    casos = int(input())
    t_new = ''
    for l in texto:
        posição = ord(l)-casos

        if(posição < 65):
            t_new += chr(91-(65-posição))
        else:
            t_new += chr(ord(l)-casos)
    print(t_new)