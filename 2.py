x=1
y=2
sum=0
while True:
    x+=y
    if x>4000000:
        break
    if x%2==0:
        sum+=x
    y+=x
    if y>4000000:
        break
    if y%2==0:
        sum+=y
print(sum+2)
