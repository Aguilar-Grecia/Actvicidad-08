def menu():
    print("---MENÚ PRINCIPAL DEL SISTEMA---")
    print("1. Calcular el factorial de un número.")
    print("2. Suma de los primeros N números naturales.")
    print("3. Calcular el n-ésimo número de Fibonacci.")
    print("4. Contar cuántas veces aparece una letra en una plabra.")
    print("5. Invertir una cadena de texto.")
    print("6. Calcular la potencia de un número")
    print("7. Salir del programa.")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def suma_n(n):
    if n == 0:
        return 0
    else:
        return n + suma_n(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
