from quickSort import quick_sort


def bucket_sort(arr):
    bucket = []

    #Estou criando uma quantidade de baldes vazios do tamanho do array
    for i in range(len(arr)):
        bucket.append([])
    
    #Colocando os elementos nos baldes -  os baldes têm 10 elementos, os valores de 0 a 9 ficarão todos no balde ZERO
    for i in arr:
        bucketIndex = int(i/10)
        bucket[bucketIndex].append(i)

    #Ordenando cade balde individualmente com o quicksort
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])
    
    #Juntando tudo em um array
    k = 0
    for i in range(len(arr)):
        for j in range (len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

    