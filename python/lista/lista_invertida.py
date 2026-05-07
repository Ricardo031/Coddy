def reverse(numbers):
    reversed_list = []
    n = len(numbers)
    
    # Recorremos desde 0 hasta n-1 para cubrir todos los elementos
    for i in range(n):
        # Accedemos en orden inverso usando n - i - 1
        reversed_list.append(numbers[n - i - 1])
        
    return reversed_list

# Ejemplo de uso
if __name__ == "__main__":
    lista = [1, 2, 3 ]
    print(f"Original: {lista}")
    print(f"Invertida: {reverse(lista)}")
