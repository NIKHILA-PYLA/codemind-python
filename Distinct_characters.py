a=input()
arr=[]
for i in range(len(a)):
    if a[i].isspace():
        continue
    if a[i].upper() not in a[:i] and a[i].upper() not in a[i+1:]:
        if a[i].lower() not in a[:i] and a[i].lower() not in a[i+1:]:
                arr.append(a[i])
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in arr:
    print(i,end="")
if len(arr)==0:
    print(0)
