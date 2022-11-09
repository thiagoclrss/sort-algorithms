import random 
from bubbleSort import bubble_sort
from selectionSort import selection_sort
from insertionSort import insertion_sort
from quickSort import quick_sort
import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt
import sys

any_numbers =  random.sample(range(1,1000), 42)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28,   
32, 34, 76, 39, 40, 42, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]    

if __name__ == "__main__":
    test_cases = {'Números aleatórios': any_numbers,
                    'Já ordenados': already_sorted,
                    'Ordem inversa': inversed,
                    'Elementos repetidos':repeated    
                }
    print("******************")
    for name, lista in test_cases.items():
        print("\nCaso de teste: {}".format(name))
        print(lista)
        quick_sort(lista)
        print("\n Ordenado:")
        print(lista)
    print("******************")







"""    
def graf():
    tempo = []
    tamListas = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]
    for x in tamListas:
        lista = np.random.randint(0,300,x)
        inicio = perf_counter()
        bubble_sort(lista)
        print("\n Ordenado:")
        fim = perf_counter()
        duracao = fim - inicio
        tempo.append(duracao)
        print(duracao)
    return tempo, tamListas

tmp, ta = graf()

plt.plot(ta, tmp)
plt.show()

# O pior caso é quando a lista está invertida
def grafPiorCaso():
    tempo = []
    tamListas = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]
    for x in tamListas:
        lista = np.random.randint(0,300,x)
        listaInvertida = sorted(lista, key = int, reverse = True)
        inicio = perf_counter()
        bubble_sort(listaInvertida)
        print("\n Ordenado:")
        fim = perf_counter()
        duracao = fim - inicio
        tempo.append(duracao)
        print(duracao)
    return tempo, tamListas

tmp2, ta2 = grafPiorCaso()

plt.plot(ta2, tmp2)
plt.show()
"""
'''
if __name__ == "__main__":
    lista = repeated
    print(lista)
    selection_sort(lista)
    print("\n Ordenado: ")
    print(lista)
'''
'''
def graf():
    tempo = []
    tamListas = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]
    sys.recursivelimits(100000)
    for x in tamListas:
        lista = np.random.randint(0,100000,x)
        inicio = perf_counter()
        quick_sort(lista)
        fim = perf_counter()
        duracao = fim - inicio
        tempo.append(duracao)
        print("\n Ordenado:")
        print(duracao)
    return tempo, tamListas

tmp, ta = graf()

# O pior caso é quando a lista está invertida
def grafPiorCaso():
    tempo = []
    tamListas = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]     
    for x in tamListas:
        listaInvertida = [i for i in range(x,0,-1)]
        sys.recursivelimits(100000)
        inicio = perf_counter()
        quick_sort(listaInvertida)
        fim = perf_counter()
        duracao = fim - inicio
        tempo.append(duracao)
        print("\n Ordenado:")
        print(duracao)
    return tempo, tamListas

tmp2, ta2 = grafPiorCaso()

plt.plot(ta,tmp)
plt.plot(ta2,tmp2,label = 'pior caso')
plt.xlabel('Tamanho')
plt.ylabel('Tempo')
plt.legend(loc='upper right')
plt.show()
'''
sys.setrecursionlimit(100000)
def graf():
    tempo = []
    tamListas = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]
    #sys.setrecursionlimit(10000)
    for x in tamListas:
        lista = np.random.randint(0,1000,x)
        inicio = perf_counter()
        quick_sort(lista)
        fim = perf_counter()
        duracao = fim - inicio
        tempo.append(duracao)
        print("\n Ordenado:")
        print(duracao)
    return tempo, tamListas

tmp, ta = graf()




def grafPiorCaso():
    tempo = []
    tamListas = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000] 
    #sys.setrecursionlimit(10000)    
    for x in tamListas:
        lista = np.random.randint(0,100000,x)
        listaInvertida = sorted(lista, key = int, reverse = True)
        inicio = perf_counter()
        quick_sort(listaInvertida)
        fim = perf_counter()
        duracao = fim - inicio
        tempo.append(duracao)
        print("\n Ordenado:")
        print(duracao)
    return tempo, tamListas

tmp2, ta2 = grafPiorCaso()

plt.plot(ta,tmp)
plt.plot(ta2,tmp2,label = 'pior caso')
plt.xlabel('Tamanho')
plt.ylabel('Tempo')
plt.legend(loc='upper right')
plt.show()
