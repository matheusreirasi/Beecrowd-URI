N=int(input())
v=[0]*N
p=[]
im=[]

for i in range(N):
    v[i]=int(input())
    if v[i]%2==0:
        p.append(v[i])
    if v[i]%2!=0:
        im.append(v[i])
        
for i in range(len(p)):
    for j in range(len(p)-1):
        if p[j] > p[j+1]:
            p[j],p[j+1] = p[j+1],p[j]
for i in range(len(im)):
    for j in range(len(im)-1):
        if im[j] < im[j+1]:
            im[j],im[j+1] = im[j+1],im[j]
print(p+im)

#DEU TIME LIMIT NO BEECROWD