import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt

def bubble_sort(lista):
    n =  len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                #em python posso fazer assim para trocar de lugar os valores de uma lista sem criar um variável aux
                lista[i], lista[i+1] = lista[i+1], lista[i]
