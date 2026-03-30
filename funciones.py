# argumentos
def is_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


for i in range(15, 20):
    is_even(i)
for i in range(153, 156):
    is_even(i)
print("--------------------------------------------------")


# Declare your function here
# print the result of a*b inside the function
def multi(a, b):
    # ? result = a * b esto es una manera
    # ? print(result)
    return a * b


a = int(input())
b = int(input())
# Call your function here with the arguments a and b
c = multi(a, b)
print(c)
# y este es otra manera que hace lo mismo

# ? multi(a,b)
print("--------------------------------------------------")


def calculate_area(length, width):
    # Write your code below
    area = length * width
    print(area)


length = float(input())
width = float(input())
# Call the function below
calculate_area(length, width)
print("---------------------------------------------------")


def sigma(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)


n = int(input("Enter a number: "))
sigma(n)
