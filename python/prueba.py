#Factorial es una operación matemática.
num = int(input("coloca un numero: "))
var = 1
for i in range(1, num + 1):
    var *= i
print(var)



rows = 2
cols = 3
for i in range(rows):
    line = ""
    for j in range(cols): 
        line += "*"
    print(line)  
    
    
    
for i in range(2):
    for j in range(3):
        print(i, end=" ")