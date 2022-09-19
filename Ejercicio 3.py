# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 21:05:46 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


# Función que determinará los valores dentro de una lista mayores que el promedio de esta.
def mayores_que_promedio(lista):
    suma = 0  # Se inicializa la suma de los elementos de la lista como 0
    contador_datos = 0  # Se inicializa el contador de datos mayores que el promedio como 0

    for datos in lista:  # Para cada elemento de la lista
        suma += datos  # Se suma el valor del elemento y se guarda en la variable suma
        # Se calcula el promedio de la lista con la suma obtenida anteriormente
        promedio = suma / len(lista)

    for datos in lista:  # Para cada elemento de la lista
        if datos > promedio:  # Si el elemento es mayor al promedio de la lista
            contador_datos += 1  # Se incrementa en 1 el contador de datos mayores que el promedio

    return contador_datos  # Se retorna el contador de datos mayores que el promedio


# Programa principal
n = int(input("¿Cuántos datos desea ingresar?: "))

lista = []  # Se inicializa la lista vacía para luego preguntar al usuario por cada valor que desee ingresar
for n_actuales in range(n):
    num = float(input(f"Ingrese el dato {n_actuales+1}: "))
    lista.append(num)  # Se agrega el valor ingresado a la lista

# Se llama a la función y se le pasa como parámetro la lista
resultado = mayores_que_promedio(lista)

print(f"{resultado} son mayores que el promedio.")  # Resultado final
