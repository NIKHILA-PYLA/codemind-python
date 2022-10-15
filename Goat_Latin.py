a=input()
vow="aeiouAEIOU"
arr=list(a.split())
for i in range(len(arr)):
    s=""
    if arr[i][0] in vow:
        s=arr[i]+'ma'
    else:
        s=arr[i][1:]+arr[i][0]+'ma'
    for j in range(i+1):
        s+='a'
    print(s,end="")
    print("",end=" ")