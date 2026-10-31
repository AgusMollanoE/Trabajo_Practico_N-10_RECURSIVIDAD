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
# un exponente entero no negativo, utilizando la fórmula n^m = n ∗ n^(m−1), con n^0 = 1 como
# caso base. Se pide probar la función en un algoritmo general.
def potencia(num, exponente):
    if exponente == 0:
        return 1
    else:
        return num * potencia(num, exponente - 1)


# Ejercicio 4 · Conversión de decimal a binario
# Se pide crear una función recursiva en Python que reciba un número entero positivo en
# base decimal y devuelva su representación en binario como una cadena de texto.
# La representación binaria de un número utiliza solamente ceros (0) y unos (1), en base 2.
# Para convertir un número decimal a binario, se puede seguir este procedimiento:
#   1. Dividir el número por 2.
#   2. Guardar el resto (0 o 1).
#   3. Repetir el proceso con el cociente hasta que llegue a 0.
#   4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
def decimal_a_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        cociente = num // 2
        resto = num % 2
        return decimal_a_binario(cociente) + str(resto)


# Ejercicio 5 · Palíndromo
# Se pide implementar una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes y devuelva True si es un palíndromo o False si no lo
# es.
# Requisitos:
#   · La solución debe ser recursiva.
#   · No se debe usar [::-1] ni la función reversed().
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])


# Ejercicio 6 · Suma de dígitos
# Se pide escribir una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
#   · No se puede convertir el número a cadena de texto.
#   · Se deben usar operaciones matemáticas (%, //) y recursión.
def suma_digitos(num):
    if num == 0:
        return 0
    else:
        return num % 10 + suma_digitos(num // 10)


# Ejercicio 7 · Pirámide de bloques
# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último
# nivel con un solo bloque.
# Se pide escribir una función recursiva contar_bloques(n) que reciba el número de bloques
# en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
def contar_bloques(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + contar_bloques(num - 1)


# Ejercicio 8 · Apariciones de un dígito
# Se pide escribir una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
