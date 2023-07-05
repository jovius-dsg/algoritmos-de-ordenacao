def partition(lista, low, high):

  pivot = lista[high]

  i = low - 1

  for j in range(low, high):
    if lista[j] <= pivot:

      i = i + 1

      (lista[i], lista[j]) = (lista[j], lista[i])

  (lista[i + 1], lista[high]) = (lista[high], lista[i + 1])

  return i + 1

def quickSort(lista, low, high):
  
  if low < high:
    pi = partition(lista, low, high)
    quickSort(lista, low, pi - 1)
    quickSort(lista, pi + 1, high)  
  