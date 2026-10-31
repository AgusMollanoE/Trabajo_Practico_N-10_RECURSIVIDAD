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
    print("||              UTN - PROGRAMACION I              ||")
    print("||             Trabajo Práctico N° 10             ||")
    print("||                  Recursividad                  ||")
    print("||                                                ||")
    print("####################################################")

def menu_principal():

    while True:
        print("----------------------------------------------------")
        print("|                  Menu Principal                  |")
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
                print("----------------------------------------------------")
                print("| Ejercicio 1 - Factorial                          |")
                print("----------------------------------------------------")
                num = int(input("Ingrese un numero entero: "))
                # FUNCION
                #funciones.factorial(num)
                print(f"{funciones.factorial(num)}")
                pausar()
                limpiar_pantalla()

            elif opcion == 2:
                print("----------------------------------------------------")
                print("| Ejercicio 2 - Sucesión de Fibonacci              |")
                print("----------------------------------------------------")
                num = int(input("Ingrese un numero entero: "))
                # FUNCION
                print("---------------Suceción De FIBONACCI----------------")
                for i in range(num + 1):
                    resultado = funciones.fibonacci(i)
                    print("| ", resultado, end= " |")
                print("\n")
                pausar()
                limpiar_pantalla()

            elif opcion == 3:
                print("----------------------------------------------------")
                print("| Ejercicio 3 - Potencia                           |")
                print("----------------------------------------------------")
                # FUNCION
                num = int(input("Ingrese un numero entero Positivo: "))
                exp = int(input("ingrese un Exponente entero positivo: "))
                print(f"Resultado de elevar {num} a la potencia de {exp} es: {funciones.potencia(num, exp)}")
                pausar()
                limpiar_pantalla()

            elif opcion == 4:
                print("----------------------------------------------------")
                print("| Ejercicio 4 - Conversión de decimal a binario    |")
                print("----------------------------------------------------")
                # FUNCION
                num = int(input("Ingrese un numero: "))
                print(funciones.decimal_a_binario(num))
                pausar()
                limpiar_pantalla()
            
            elif opcion == 5:
                print("----------------------------------------------------")
                print("| Ejercicio 5 - Palíndromo                         |")
                print("----------------------------------------------------")
                # FUNCION
                funciones.palindromo()
                pausar()
                limpiar_pantalla()
            
            elif opcion == 6:
                print("----------------------------------------------------")
                print("| Ejercicio 6 - Suma de dígitos                    |")
                print("----------------------------------------------------")
                # FUNCION
                funciones.suma_digitos()
                pausar()
                limpiar_pantalla()
            
            elif opcion == 7:
                print("----------------------------------------------------")
                print("| Ejercicio 7 - Pirámide de bloques                |")
                print("----------------------------------------------------")
                # FUNCION
                funciones.piramide_bloques()
                pausar()
                limpiar_pantalla()

            elif opcion == 8:
                print("----------------------------------------------------")
                print("| Ejercicio 8 - Apariciones de un dígito           |")
                print("----------------------------------------------------")
                # FUNCION
                funciones.aparicion_digito()
                pausar()
                limpiar_pantalla()
        
            elif opcion == 0:
                print("----------------------------------------------------")
                print("| ¡Hasta luego!                                    |")
                print("----------------------------------------------------\n")
                break

            else:
                raise ValueError("Opción inválida. Seleccione una opción entre (1 - 8).")  
                
        except ValueError as e:
            print(f"\nERROR: {e}\n")
            pausar()
            limpiar_pantalla()
