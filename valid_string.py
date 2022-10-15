from statistics import *
s=input()
ar=[]
c=0
for i in s:
    ar.append(s.count(i))
m=mode(ar)
for i in s:
    if s.count(i)!=m:
        if c<1:
            c+=1
        else:
            print("Not Valid")
            break
else:
    print("Valid String")