a=int(input())
while a>0:
    if a>=1000:
        print("M",end="")
        a-=1000
    elif a>=900:
        print("CM",end="")
        a-=900
    elif a>=500:
        print("D",end="")
        a-=500
    elif a>=400:
        print("CD",end="")
        a-=400
    elif a>=100:
        print("C",end="")
        a-=100
    elif a>=90:
        print("XC",end="")
        a-=90
    elif a>=50:
        print("L",end="")
        a-=50
    elif a>=40:
        print("XL",end="")
        a-=40
    elif a>=10:
        print("X",end="")
        a-=10
    elif a==9:
        print("IX",end="")
        a-=9
    elif a==8:
        print("VIII",end="")
        a-=8
    elif a==7:
        print("VII",end="")
        a-=7
    elif a==6:
        print("VI",end="")
        a-=6
    elif a==5:
        print("V",end="")
        a-=5
    elif a==4:
        print("IV",end="")
        a-=4
    elif a==3:
        print("III",end="")
        a-=3
    elif a==2:
        print("II",end="")
        a-=2
    elif a==1:
        print("I")
        a-=1
