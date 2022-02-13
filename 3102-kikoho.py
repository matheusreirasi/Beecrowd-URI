<<<<<<< HEAD
casos = int(input())
x1,y1,x2,y2,x3,y3 = input().split()


while casos >= 1:
    pontoA = [int(x1),int(y1)]
    pontoB = [int(x2),int(y2)]
    pontoC = [int(x3),int(y3)]
    AB,BC,CA = 0,0,0
    todasBases = []
    for i in range(2):
        AB+=pontoB[i]-pontoA[i]
        BC+=pontoC[i]-pontoB[i]
        CA+=pontoA[i]-pontoC[i]
    soma = (AB+BC+CA)/2
    area = (soma*(soma-AB)*(soma-BC)*(soma-CA)**0.5)
    casos -= 1
print(AB)

#    todasBases = AB,BC,CA
#    base = []
#    for i in range(len(todasBases)):
#        if todasBases[i] > todasBases[i+1]:
#            base.append(todasBases[i])
#    for i in range(3):
=======
casos = int(input())

while casos >= 1:
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    area = abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    casos -= 1
    print("%.3f"%area)
>>>>>>> alternativo
