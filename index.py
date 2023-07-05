from bubble_sort import *
from heap_sort import *
from inserção_simples import *
from merge_sort import *
from quick_sort import *
from selecao_direta import *
from shell_sort import *

import time
import random

def criacao_dados(n):
    random.seed(30)
    lista = []
    for i in range(n):
        lista.append(random.randrange(1, 100))
    return lista

def buble_sort ():
    n = 1
    for i in range (1,5):
        n = n*10
        lista = criacao_dados(n)

        # Bubble Sort #
        inicio = time.perf_counter_ns()
        bubbleSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        print("Bubble Sort")
        print(f'n = {n} Tempo de execução: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000000} em segundos')
        print("---------------------------------------------------------", "\n")

def heap_sort ():
    n = 1
    for i in range (1,5):
        n = n*10
        lista = criacao_dados(n)

        # Heap Sort #
        inicio = time.perf_counter_ns()
        heapSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        print("Heap Sort")
        print(f'n = {n} Tempo de execução: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000000} em segundos')
        print("---------------------------------------------------------", "\n")     

def isercao_simples ():
    n = 1
    for i in range (1,5):
        n = n*10
        lista = criacao_dados(n)

        # Inserção Simples #
        inicio = time.perf_counter_ns()
        insercaoSimples(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        print("Inserção Simples")
        print(f'n = {n} Tempo de execução: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000000} em segundos')
        print("---------------------------------------------------------", "\n")

def merge_sort ():
    n = 1
    for i in range (1,5):
        n = n*10
        lista = criacao_dados(n)  

        # Merge Sort #
        inicio = time.perf_counter_ns()
        mergeSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        print("Merge Sort")
        print (f'n = {n} Tempo de execução: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000000} em segundos')
        print("---------------------------------------------------------", "\n")

def quick_sort ():
    n = 1
    for i in range (1,5):
        n = n*10
        lista = criacao_dados(n)
        tamanho = len(lista)  

        # Quick Sort #
        inicio = time.perf_counter_ns()
        quickSort(lista, 0, tamanho-1)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        print("Quick Sort")
        print (f'n = {n} Tempo de execução: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000000} em segundos')
        print("---------------------------------------------------------", "\n")

def selecao_direta ():
    n = 1
    for i in range (1,5):
        n = n*10
        lista = criacao_dados(n)
        tamanho = len(lista)

        # Seleção Direta #
        inicio = time.perf_counter_ns()
        selecaoDireta(lista, tamanho)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        print("Seleção Direta")
        print (f'n = {n} Tempo de execução: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000000} em segundos')
        print("---------------------------------------------------------", "\n")

def shell_sort ():
    n = 1
    for i in range (1,5):
        n = n*10
        lista = criacao_dados(n)
        tamanho = len(lista)

        # Shell Sort #
        inicio = time.perf_counter_ns()
        shellSort(lista, tamanho)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        print("Shell Sort")
        print (f'n = {n} Tempo de execução: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000000} em segundos')
        print("---------------------------------------------------------", "\n")

def geral ():
    buble_sort()
    heap_sort()
    isercao_simples()
    merge_sort()
    quick_sort()
    selecao_direta()
    shell_sort()

    return True

geral()