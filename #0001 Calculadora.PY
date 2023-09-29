# Calculadora hecha en Python
# COD REF 0001
while True:
    print("Bienvenidos a la Calculadora Python V1.0 by Scstel")
    print("1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Calculadora Compleja \n6. Salir")

    opcion = int(input("Introduce la opción deseada: "))

    if opcion == 1:
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese otro número: "))
        print("Su resultado es: ", numero1 + numero2)
        continue
    elif opcion == 2:
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese otro número: "))
        print("Su resultado es: ", numero1 - numero2)
        continue
    elif opcion == 3:
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese otro número: "))
        print("Su resultado es: ", numero1 * numero2)
        continue
    elif opcion == 4:
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese otro número: "))
        if numero2 != 0:
            print("Su resultado es: ", numero1 / numero2)
            continue
        else:
            print("Error: No se puede dividir por 0.")
            continue
    elif opcion == 5:
        cantidad1 = float(input("Ingrese la primera cantidad: "))
        proporcion1 = float(input("Ingrese la primera proporción: "))
        proporcion2 = float(input("Ingrese la segunda proporción: "))
        cantidad2 = (proporcion2 * cantidad1) / proporcion1
        print("El resultado de la regla de tres es: ", cantidad2)
        continue
    elif opcion == 6:
        print("Gracias por usar la Calculadora Python V1.0. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

# Copyright 2023, scstel
