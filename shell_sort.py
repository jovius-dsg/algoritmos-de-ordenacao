def shellSort(lista, n):

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = lista[i]
            j = i
            while j >= interval and lista[j - interval] > temp:
                lista[j] = lista[j - interval]
                j -= interval

            lista[j] = temp
        interval //= 2

n = 1
for i in range (1,5):
    n = n*10
    