def mail(s):
    i1=i2=0
    for i in range(len(s)):
        if s[i]=='+':
            i1=i
        if s[i]=='@':
            i2=i
    name=""
    for i in range(i1+1):
        if s[i]=='.':
            continue
        else:
            name+=s[i]
    for i in range(i2,len(s)):
        name+=s[i]
    return name
t=int(input())
arr=[]
c=0
for i in range(t):
    a=input()
    s=mail(a)
    arr.append(s)
arr2=[]
for i in arr:
    if i not in arr2:
        arr2.append(i)
print(len(arr2))