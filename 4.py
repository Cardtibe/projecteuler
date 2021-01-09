l=[]
for i in range(1000,900,-1):
    for x in range(1000,900,-1):
        l.append(str(i)+str(x))
for i in l:
    print(i)
    q=int(i[0]+i[1]+i[2])
    w=int(i[3]+i[4]+i[5])
    t=str(q*w)
    ts=0
    for i in range(0,len(t)):
        if t[i]!=t[-i-1]:
            ts=1
    if ts==0:
        print(q*w)
        break
