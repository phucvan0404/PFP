
# 4
print("Nhập số a: ", end="")
a = float(input())

print("Nhập số b: ", end="")
b = float(input())

print("Nhập số c: ", end="")
c = float(input())

print("Nhập số x: ", end="")
x = float(input())

# 5
S1 = a*x*x + b*x + c

# 6
S2 = b*b - 4*a*c
if S2 > 0:
    S2 = S2**(0.5)
else:
    S2 = 0

print("S1: {0}\nS2: {1}".format(S1, S2))

# 7
print("Nhập số a: ", end="")
a = float(input())

print("Nhập số b: ", end="")
b = float(input())

print("Nhập số c: ", end="")
c = float(input())

# 8
if a < b+c and b < a+c and c < a+b:
    C = (a+b+c)
    p = C/2
    S1 = (p*(p-a)*(p-b)*(p-c))**(0.5)
    print("a, b, c are a side of triangle")
    print("Perimeter:", C)
    print("Area: ", S1)
else:
    print("a, b, c are not a side of triangle")