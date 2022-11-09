import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt

def heap(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
 # See if left child of root exists and is
 # greater than root
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
 # See if right child of root exists and is
 # greater than root
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
 # Change root, if needed
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
 
  # Heapify the root.
 
        heap(arr, n, largest)
 
 
# The main function to sort an array of given size
 
def heapSort(arr):
    n = len(arr)
 
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
 
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)
 
 # One by one extract elements
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heap(arr, i, 0)
 

def graf():
    tempo = []
    tamListas = [10000,20000,40000,70000,100000,500000]
    for x in tamListas:
        lista = np.random.randint(0,100000,x)
        inicio = perf_counter()
        heapSort(lista)
        fim = perf_counter()
        duracao = fim - inicio
        tempo.append(duracao)
        print("\n Ordenado:")
        print(duracao)
    return tempo, tamListas

tmp, ta = graf()


plt.plot(ta,tmp)
plt.xlabel('Tamanho')
plt.ylabel('Tempo')
plt.show()