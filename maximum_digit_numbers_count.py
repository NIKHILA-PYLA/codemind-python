a=int(input())
b=input()
arr=list(b.split())
ma=0
for i in arr:
    if len(i)>ma:
        ma=len(i)
c=0
for i in arr:
    if len(i)==ma:
        print(i,end=" ")

