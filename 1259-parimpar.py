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

p.sort()
im.sort(reverse=True)
ordem=p+im

for i in range(len(ordem)):
    print(ordem[i])