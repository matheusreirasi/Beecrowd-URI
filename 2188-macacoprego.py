região=int(input())

while região!=0:
    for i in range(região):
        x1 , y1 , x2 , y2 = input().split()
        distancia = (abs(int(x2)) - abs(int(x1)) + abs(int(y2)) - abs(int(y1)))
print(distancia)