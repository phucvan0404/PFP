
# 1
number1 = 20
number2 = 30
print("The result is", number1*number2)

number1 = 40
number2 = 30

print("The result is", number1+number2)


# 2
print("Printing current and previous number sum in a range(10)")
for i in range(10):
    if i == 0:
        print("Current Number 0 Previous Number 0 Sum: 0")
    else:
        print("Current Number {0} Previous Number {1} Sum: {2}".format(i,i-1,2*i-1))


# 3
print("{0}**{1}**{2}".format("Name", "Is", "James"))


