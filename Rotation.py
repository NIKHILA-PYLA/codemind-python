t=int(input())
for k in range(t):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(b):
        ft=arr[0]
        arr[0]=arr[a-1]
        for j in range(1,a):
            temp=arr[j]
            arr[j]=ft
            ft=temp
    for i in range(a):
        if i<a-1:
            print(arr[i],end=" ")
        else:
            print(arr[i])