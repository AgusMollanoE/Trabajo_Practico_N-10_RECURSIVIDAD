# Ejercicio 1 · Factorial
# Se pide crear una función recursiva que calcule el factorial de un número entero no
# negativo y utilizarla para calcular y mostrar en pantalla el factorial de todos los números
# enteros entre 1 y el número que indique el usuario.
def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num - 1) * num  

# Ejercicio 2 · Sucesión de Fibonacci
# Se pide crear una función recursiva que calcule el valor de la sucesión de Fibonacci en la
# posición indicada. Posteriormente, se pide mostrar la sucesión completa hasta la posición
# que especifique el usuario.
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# Ejercicio 3 · Potencia
# Se pide crear una función recursiva que calcule la potencia de un número base elevado a
# un exponente entero no negativo, utilizando la fórmula n elevado m = n ∗ n (m−1), con n 0 = 1 como
# caso base. Se pide probar la función en un algoritmo general.
def potencia(num, exponente):
    if exponente == 0:
        return 1
    else:
        return  num * potencia(num, exponente - 1)
    

def decimal_a_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        cosiente = num // 2
        resto = num % 2
        return decimal_a_binario(cosiente) + str(resto)

def palindromo():
    pass

def suma_digitos():
    pass

def piramide_bloques():
    pass

def aparicion_digito():
    pass    