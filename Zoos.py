a=input()
zc=oc=0
for i in a:
    if i=='z':
        zc+=1
    elif i=='o':
        oc+=1
if zc*2==oc:
    print("Yes")
else:
    print("No")