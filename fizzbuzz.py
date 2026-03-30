# por ahora veo 2 soluciones
# todo. Esta es mi solucion
# print("Welcome to FizzBuzz!")

# def FizzBuzz(num):
#     if num % 3 == 0 and num % 7 == 0:
#         return "FizzBuzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     elif num % 7 == 0:
#         return "Buzz"
#     else:
#         return str(num)


# num = int(input())
# result = FizzBuzz(num)
# print(result)

# #todo. y esta es la de la maquina. pues se ve
# print("Welcome to FizzBuzz!")

# def fizzbuzz(number):
#     result = ""
#     if number % 3 == 0:
#         result += "Fizz"
#     if number % 7 == 0:
#         result += "Buzz"
#     if result == "":
#         result = str(number)
#     return result

# limit = int(input())
# print(fizzbuzz(limit)) #la verdad si se ve bien e inclusivo mas escalable pero igual el mio soluciona por ahora

print("Welcome to FizzBuzz!")


def FizzBuzz(num):
    result = ""
    for i in range(1, num + 1):
        if i % 3 == 0:
            result += "Fizz"
            print(result)
            continue
        if i % 7 == 0:
            result += "Buzz"
        if i == "":
            result += str(num)
        print(i)
    return result


num = int(input("enter a number: "))
FizzBuzz(num)
