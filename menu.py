import os
import funciones

# Funciones para uso del sistema. Limpiar y pausar la terminal.
def limpiar_pantalla():
    os.system("cls")

def pausar():
    os.system("pause")

limpiar_pantalla()

def presentacion():
    print("####################################################")
    print("||                                                ||")
    print("||              UTN - PROGRAMACIÓN I              ||")
    print("||             Trabajo Práctico N° 10             ||")
    print("||                  Recursividad                  ||")
    print("||                                                ||")
    print("####################################################")

def menu_principal():
    while True:
        print("----------------------------------------------------")
        print("|                  Menú principal                  |")
        print("----------------------------------------------------")
        print("| 1. Ejercicio 1 - Factorial                       |")
        print("| 2. Ejercicio 2 - Sucesión de Fibonacci           |")
        print("| 3. Ejercicio 3 - Potencia                        |")
        print("| 4. Ejercicio 4 - Conversión de decimal a binario |")
        print("| 5. Ejercicio 5 - Palíndromo                      |")
        print("| 6. Ejercicio 6 - Suma de dígitos                 |")
        print("| 7. Ejercicio 7 - Pirámide de bloques             |")
        print("| 8. Ejercicio 8 - Apariciones de un dígito        |")
        print("| 0. Salir                                         |")
        print("----------------------------------------------------")

        try:
            opcion = int(input("Seleccione una opción: "))
            limpiar_pantalla()

            if opcion == 1:
                print("\n----------------------------------------------------")
                print("| Ejercicio 1 - Factorial                          |")
                print("----------------------------------------------------")
                num = int(input("Ingrese un número entero: "))
                if num < 0:
                    raise ValueError("El número debe ser un entero no negativo.")
                # FUNCION
                print("\n-------------------Factoriales---------------------")
                if num == 0:
                    print(f"El factorial de 0 es: 1")
                else:
                    for i in range(1, num + 1):
                        print(f"El factorial de {i} es: {funciones.factorial(i)}")
                print("\n")
                pausar()
                limpiar_pantalla()

            elif opcion == 2:
                print("\n----------------------------------------------------")
                print("| Ejercicio 2 - Sucesión de Fibonacci              |")
                print("----------------------------------------------------")
                num = int(input("Ingrese un número entero: "))
                if num < 0:
                    raise ValueError("El número debe ser un entero no negativo.")
                # FUNCION
                print("\n---------------Sucesión De Fibonacci----------------")
                for i in range(num + 1):
                    resultado = funciones.fibonacci(i)
                    print("|", resultado, end=" |")
                print("\n")
                pausar()
                limpiar_pantalla()

            elif opcion == 3:
                print("\n----------------------------------------------------")
                print("| Ejercicio 3 - Potencia                           |")
                print("----------------------------------------------------")
                num = int(input("Ingrese un número entero: "))
                if num < 0:
                    raise ValueError("El número debe ser un entero no negativo.")
                exp = int(input("Ingrese un exponente entero: "))
                if exp < 0:
                    raise ValueError("El exponente debe ser un entero no negativo.")
                # FUNCION
                print(f"\nResultado de elevar {num} a la potencia de {exp} es: {funciones.potencia(num, exp)}\n")
                pausar()
                limpiar_pantalla()

            elif opcion == 4:
                print("\n----------------------------------------------------")
                print("| Ejercicio 4 - Conversión de decimal a binario    |")
                print("----------------------------------------------------")
                num = int(input("Ingrese un número entero: "))
                if num < 0:
                    raise ValueError("El número debe ser un entero no negativo.")
                # FUNCION
                print(f"\nEl número {num} en binario es: {funciones.decimal_a_binario(num)}\n")
                pausar()
                limpiar_pantalla()

            elif opcion == 5:
                print("\n----------------------------------------------------")
                print("| Ejercicio 5 - Palíndromo                         |")
                print("----------------------------------------------------")
                palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
                if not palabra.isascii() or not palabra.isalpha():
                    raise ValueError("La palabra debe contener solo letras sin tildes.")
                # FUNCION
                if funciones.es_palindromo(palabra):
                    print(f"\nLa palabra '{palabra}' es un palíndromo.\n")
                else:
                    print(f"\nLa palabra '{palabra}' no es un palíndromo.\n")
                pausar()
                limpiar_pantalla()

            elif opcion == 6:
                print("\n----------------------------------------------------")
                print("| Ejercicio 6 - Suma de dígitos                    |")
                print("----------------------------------------------------")
                num = int(input("Ingrese un número entero: "))
                if num < 0:
                    raise ValueError("El número debe ser un entero no negativo.")
                # FUNCION
                print(f"\nLa suma de los dígitos de {num} es: {funciones.suma_digitos(num)}\n")
                pausar()
                limpiar_pantalla()

            elif opcion == 7:
                print("\n----------------------------------------------------")
                print("| Ejercicio 7 - Pirámide de bloques                |")
                print("----------------------------------------------------")
                num = int(input("Ingrese un número entero: "))
                if num < 0:
                    raise ValueError("El número debe ser un entero no negativo.")
                # FUNCION
                print(f"\nEl total de bloques necesarios para construir la pirámide es: {funciones.contar_bloques(num)}\n")
                pausar()
                limpiar_pantalla()

            elif opcion == 8:
                print("\n----------------------------------------------------")
                print("| Ejercicio 8 - Apariciones de un dígito           |")
                print("----------------------------------------------------")
                numero = int(input("Ingrese un número entero: "))
                if numero < 0:
                    raise ValueError("El número debe ser un entero no negativo.")
                digito = int(input("Ingrese un dígito (0-9): "))
                if digito < 0 or digito > 9:
                    raise ValueError("El dígito debe estar entre 0 y 9.")
                # FUNCION
                contador = funciones.contar_digito(numero, digito)
                if contador == 1:
                    print(f"\nEl dígito {digito} aparece {contador} vez en el número {numero}.\n")
                else:
                    print(f"\nEl dígito {digito} aparece {contador} veces en el número {numero}.\n")
                pausar()
                limpiar_pantalla()

            elif opcion == 0:
                print("\n----------------------------------------------------")
                print("| ¡Hasta luego!                                    |")
                print("----------------------------------------------------\n")
                break

            else:
                raise ValueError("Opción inválida. Seleccione una opción entre (1 - 8).")

        except ValueError as e:
            print(f"\nERROR: {e}\n")
            pausar()
            limpiar_pantalla()
