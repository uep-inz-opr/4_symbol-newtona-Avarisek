import math
x,y=input().split(" ")
x=int(x)
y=int(y)

if y==1 or y==x:
    print(1)

if y>x:
    print(1)
else:
    liczba1=math.factorial(x)
    liczba2=math.factorial(y)
    liczba3=math.factorial(x-y)
    dzielenie= liczba1//(liczba2*liczba3)
    print(dzielenie)