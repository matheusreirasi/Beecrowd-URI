nRegiões=int(input())
xx=-10000
yy=10000
uu=10000
vv=-10000
teste=0

while nRegiões != 0:
    for i in range(nRegiões):
        x , y , u , v = map(int, (input().split()))
        if x > xx and x < uu:
            xx=x
        if y > vv and y < yy:
            yy=y
        if u > xx and u < uu:
            uu=u
        if v < yy and v > vv:
            vv=v
    teste+=1
    print("Teste ",teste)
    print(xx,yy,uu,vv)