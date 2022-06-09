def get_input(title):
    s = str(input(title))
    return s

def valid_int(n):
    try:
        k = int(n)
        return 1
    except:
        return 0



n = get_input("Enter integer number n: ")
while not valid_int(n):
    n = get_input("Enter integer number n: ")
n = int(n)
print(f"{n} in binary format is: {str(bin(int(n)))[2:]}")

n = get_input("Please re-input n: ")
_sum = sum([int(i) for i in str(n)])
print(f"Sum of digit n is: {_sum}")

print(f"Number m is: {int(str(n)[::-1])}")