import math
asal=[2,3]
def sas():
    x=asal[-1]
    con=0
    while True:
        x+=1
        for i in asal:
            if x%i==0:
                con=1
        if con==0:
            return x
        else:
            con=0
num=600851475143
max=0
while num>1:
    for i in asal:
        while num%i==0:
            num=num/i
            max=i
    asal.append(sas())
    print(asal[-1])
print(max)
