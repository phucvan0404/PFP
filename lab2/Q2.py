def showEmployee(name, salary=9000):
    print(f"Name: {name} salary: {salary}")

showEmployee("Ben", 12000)
showEmployee("Jessa")


def outer_func(a, b):

    def inner_func(a, b):
        return a+b
    
    return inner_func(a, b) + 5

res = outer_func(5, 10)
print(res)