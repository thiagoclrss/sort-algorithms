
lista = [2,3,5,2,2,1,2,3,12]
print(lista)
def counting_sort(lista):
    N = len(lista)
    M = max(lista) + 1
    out = [0] * N    
    count = [0] * (M)
    
    for i in range(1, N):
        count[lista[i]] += 1
    print(count)

    for i in range (1, M):
        count[i] += count[i-1]

    t = N - 1
    while t >= 0: 
        out[count[lista[t]]-1] = lista[t]
        count[lista[t]] -= 1
        t-=1
    
    for i in range(0,N):
        lista[i] = out[i]

counting_sort(lista)
print(lista)    
'''
    print(out)
x = counting_sort(lista)
print(x)
 
lista input
lista de indices do tamanho do valor max da lista input
arr de contagem zerado do mesmo tamanho para contarmos as repetições da entrada
contadas as repetições da lista input no arr de contagem somamos o valor da posição atual com a anterior(i= i + (i-1))
    """
for j in range (0, M+1):
    k = count[j]
    i = 0
    while(k > 0):
        if k == 0:
            break
        out[i] = j
        print(out)
           
        k -= 1
"""

    '''
"""
rodou:
def countingSort(arr):
    size = len(arr)
    output = [0] * size
    N = max(arr) + 1

    # count array initialization
    count = [0] * N

    # storing the count of each element 
    for m in range(0, size):
        count[arr[m]] += 1

    # storing the cumulative count
    for m in range(1, N):
        count[m] += count[m - 1]

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    for m in range(0, size):
        arr[m] = output[m]

data = [2,3,5,2,2,1,2,3,12]
countingSort(data)
print("Sorted Array: ")
print(data)
"""