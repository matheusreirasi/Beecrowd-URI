N=int(input())
n=0

while N > 0:
    xx=-10000
    yy=10000
    uu=10000
    vv=-10000
    for i in range(N):
        x , y , u , v = map(int, (input().split()))
        if x > xx and x < uu:
            xx=x
        if y > vv and y < yy:
            yy=y
        if u > xx and u < uu:
            uu=u
        if v < yy and v > vv:
            vv=v
    n+=1
    print("Teste",n)

    if (u<xx or v>yy or x>uu or y<vv or N<=1):
        print("nenhum","\n")
    else:
        print(xx,yy,uu,vv,"\n")
    
    N=int(input())