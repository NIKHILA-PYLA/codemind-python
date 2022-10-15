a=input()
arr=[]
for i in range(len(a)):
    rc=lc=0
    ind=0
    for j in range(i):
        if a[j]=='R':
            rc+=1
        if a[j]=='L':
            lc+=1
        ind=j
    if rc==lc:
        arr.append(a[i:ind])
print(len(arr))