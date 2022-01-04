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
    p.sort()
for i in range(len(im)):
    im.sort(reverse=True)

print(p+im)

#DEU TIME LIMIT NO BEECROWD