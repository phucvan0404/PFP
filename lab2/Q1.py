

def func1(*args):
    print("Printing values")
    for i in args:
        print(i)


func1(20, 40, 60)
func1(80, 100)

def calculation(a, b):
    return a+b, a-b


res = calculation(40, 10)
print(res)

