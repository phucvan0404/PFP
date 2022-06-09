def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return int(a*b/gcd(a, b))

def is_prime(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i==0:
            return 0
    return 1

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
if a > b:
    a, b = b, a
div_a = {}
for i in range(2, int(a**0.5) + 1):
    if a%i == 0:
        if is_prime(i):
            div_a[i] = 1
        if is_prime(int(a/i)):
            div_a[a/i] = 1
if is_prime(a):
    div_a[a] = 1

all_common = []
for i in range(1, int(b**0.5) + 1):
    if b%i == 0:
        if i in div_a and str(i) not in all_common:
            all_common.append(str(i))
        if int(b/i) in div_a and str(int(b/i)) not in all_common:
            all_common.append(str(int(b/i)))

print("All Common prime :", " ".join(all_common))

print(f"GCD(a, b) = {gcd(a, b)}")
print(f"LCM(a, b) = {lcm(a, b)}")