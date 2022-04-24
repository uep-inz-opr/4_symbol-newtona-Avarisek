import math
x=input()
y=input()
x=int(x)
y=int(y)

if y==1 or y==x:
    print(1)

if y>x:
    print(1)
else:
    liczba1=math.factorial(x)
    liczba2=math.factorial(y)
    dzielenie= liczba1//(liczba2*(x-y))
    print(dzielenie)