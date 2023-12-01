def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

while True:
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingresa el número de la operación deseada: ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {division(num1, num2)}")
        else:
            print("Opción no válida")
    else:
        print("Opción no válida. Por favor, selecciona una operación válida.")
