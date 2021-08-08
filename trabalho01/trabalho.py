import random
import math
import time


# ---- FUNÇÃO DO BUBBLESORT ----
def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if(list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]


# --- FUNÇÕES DO QUICKSORT ---
# A função partição serve para seleção do pivô e particionamento do array
def partition(list, start, end):
    pivot = list[start]

    # Particionando array
    i = start
    j = end

    while i <= j:
        # Procurar um elemento maior que meu pivô
        while(list[i] <= pivot):
            i += 1
            if(i == end):
                break

        # Procura um elemento menor que o pivô
        while(pivot <= list[j]):
            j -= 1
            if(j == start):
                break

        if i >= j:
            break

        list[i], list[j] = list[j], list[i]

    list[start], list[j] = list[j], list[start]
    return j


def quickSort(list, start, end):
    if(start >= end):
        return

    pivot = partition(list, start, end)

    quickSort(list, start, pivot - 1)
    quickSort(list, pivot + 1, end)


def generateRandomNum(list):
    for x in range(10000):
        num = random.randint(1, 100000)
        list.append(num)


# ======= INICIO DO PROGRAMA =======
# Gera a lista inicial com os números aleatórios
startList = []
generateRandomNum(startList)

# Para que seja possível comparar cada tipo de ordenação igualmente, devemos
# utilizar a mesma lista. Para que isso seja possível, separamos as lista
# de cada um.
listQuick = startList
listBubble = startList

# --- EXECUÇÃO DO QUICKSORT
# Guarda o tempo inicial para comparar com o tempo final
startChronometer = time.time()
quickSort(listQuick, 0, len(listQuick) - 1)
stopChronometer = time.time()

totalTimeQuickSort = (stopChronometer - startChronometer) * 1000
print("Tempo total de execução do Quicksort = {}ms".format(str(totalTimeQuickSort)))

# --- EXECUÇÃO DO BUBBLESORT
# Guarda o tempo inicial para comparar com o tempo final
startChronometer = time.time()
bubbleSort(listBubble)
stopChronometer = time.time()

totalTimeBubbleSort = (stopChronometer - startChronometer) * 1000
print("Tempo total de execução do Bubblesort = {}ms".format(
    str(totalTimeBubbleSort)))
