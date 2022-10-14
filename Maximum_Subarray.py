a=int(input())
arr=list(map(int,input().split()))
m=-1000
s=0
for i in range(a):
    s=0
    for j in range(i,a):
        s+=arr[j]
        if m<s:
            m=s
print(m)