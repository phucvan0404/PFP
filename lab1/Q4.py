
# 3
print("Nhập số a: ", end="")
a = float(input())

print("Nhập số b: ", end="")
b = float(input())

print("Nhập số c: ", end="")
c = float(input())

print("Maximum is:", max(a,b,c))
print("Minimun is:", min(a,b,c))

# 4

arr = sorted([a, b, c])
arr = [str(i) for i in arr]
print("<=".join(arr))

