def menu():
    print("---MENÚ PRINCIPAL DEL SISTEMA---")
    print("1. Calcular el factorial de un número.")
    print("2. Suma de los primeros N números naturales.")
    print("3. Calcular el n-ésimo número de Fibonacci.")
    print("4. Contar cuántas veces aparece una letra en una palabra.")
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
        return fibonacci(n - 1)

def contar_letra(palabra, letra, indice):
    if indice < 0:
        return 0
    if palabra[indice] == letra:
        return 1 + contar_letra(palabra, letra, indice - 1)
    else:
        return contar_letra(palabra, letra, indice -1)

def cadena_texto(cadena, texto):
    if texto < 0:
        return 0
    else:
        return cadena[texto] + cadena_texto(cadena, texto - 1)

def potencia(base, exponente):
    if exponente ==0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

while True:
    menu()
    opcion = input("Por favor, selecciona una de las opciones. ")
    match opcion:
        case"1":
            try:
                n = int(input("Ingrese un número entero positivo. "))
                if n  < 0:
                    print("Recuerde que tiene que ser un numero positivo.")
                else:
                    print(f"Factorial n {n} es {factorial(n)}")
            except ValueError:
                print("Entrada inválida.")
        case "2":
            try:
                n = int(input("Ingrese un número entero que sea positivo: "))
                if n <=0:
                    print("Recuerde que el numero debe ser mayor a 0.")
                else:
                    print(f"Suma de los primeros {n} números naturales es {suma_n(n)} ")
            except ValueError:
                print("Error al ingresar, vuelve a intentarlo.")
        case "3":
            try:
                n = int(input("Ingrese el el número, y que sea positivo. "))
                if n < 0:
                    print("El número debe ser mayor o igual a 0.")
                else:
                    print(f"Fibonacci({n}) ={fibonacci(n)}")
            except ValueError:
                print("Error al ingresar, vuelve a intentarlo.")
        case "4":
            palabra = input("Ingrese una palabra: ")
            letra = input("Ingrese una letra: ")
            if len(letra) !=1:
                print("Solo ingresa una letra.")
            else:
                resultado = contar_letra(palabra, letra, len(palabra)-1)
                print(f"La letra {letra} aparece {resultado} veces en la palabra {palabra}")
        case "5":
            cadena = input("Ingrese una cadena de texto: ")
            invertida = cadena_texto(cadena, len (cadena)- 1)
            print("cadena de texto:", invertida)
        case"6":
            try:
                base = int(input("Ingrese la base, que sea entero: "))
                exponente = int(input("Ingrese la exponente, que se debe ser entero: "))
                if exponente < 0:
                    print("El exponente tiene que ser positivo.")
                else:
                    print(f"{base}^{exponente} = {potencia(base, exponente)}")
            except ValueError:
                print("Error al ingresar, vuelve a intentarlo.")
        case"7":
            print("Gracias por estar adentro del programa. ¡Nos veremos pronto!")
            break
