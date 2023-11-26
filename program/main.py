#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import heap
import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import timeit
from scipy.optimize import curve_fit
import heapq


class MySort:
    @staticmethod
    def heapify(work_list, n, i):
        largest = i  # Инициализировать наибольший элемент как корень
        left = 2 * i + 1     # левый = 2*i + 1
        right = 2 * i + 2     # правый = 2*i + 2

        # Проверка, существует ли левый дочерний элемент корня,
        # и является ли он больше, чем корень
        if left < n and work_list[i] < work_list[left]:
            largest = left

        # То же самое для правого дочернего элемента
        if right < n and work_list[largest] < work_list[right]:
            largest = right

        # Изменить корень, если нужно
        if largest != i:
            # Свап
            work_list[i], work_list[largest] = work_list[largest], work_list[i]

            # Применить heapify к корню
            MySort.heapify(work_list, n, largest)

    @staticmethod
    def heap_sort(work_list):
        n = len(work_list)

        # Построение максимальной кучи
        for i in range(n // 2 - 1, -1, -1):
            MySort.heapify(work_list, n, i)

        # Отдельное извлечение элементов из кучи
        for i in range(n-1, 0, -1):
            work_list[i], work_list[0] = work_list[0], work_list[i]  # Свап
            MySort.heapify(work_list, i, 0)


class HeapqSort:
    @staticmethod
    def heap_sort(iterable):
        # Преобразование списка в кучу
        heapq.heapify(iterable)

        # Извлечение минимальных элементов из кучи для сортировки
        return [heapq.heappop(iterable) for _ in range(len(iterable))]


class HeapSortSpeed:
    @staticmethod
    def heapify(heap, n, pos):
        'Maxheap variant of _siftup'
        endpos = n
        newitem = heap[pos]
        childpos = 2*pos + 1

        while childpos < endpos:
            rightpos = childpos + 1

            if rightpos < endpos and not heap[rightpos] < heap[childpos]:
                childpos = rightpos

            if heap[pos] < heap[childpos]:
                heap[pos] = heap[childpos]

                pos = childpos
                childpos = 2*pos + 1
            else:
                break

        heap[pos] = newitem

    @staticmethod
    def heap_sort(iterable):
        n = len(iterable)

        # Преобразование списка в кучу
        heapq._heapify_max(iterable)

        # Извлечение максимальных элементов из кучи для сортировки
        for i in range(n-1, 0, -1):
            iterable[i], iterable[0] = iterable[0], iterable[i]  # Свап
            HeapSortSpeed.heapify(iterable, i, 0)


def find_coeffs_bin(x, time):
    params, _ = curve_fit(n_log_n, np.array(x),
                          np.array(time))
    a, b = params
    return a, b


def n_log_n(x, a, b):
    return a * x * np.log(x) + b


def create_graph(b, c, namegraph):
    plt.scatter(b, c, s=5)
    aur, bur = find_coeffs_bin(b, c)
    y_line = n_log_n(np.array(b), aur, bur)
    plt.plot(b, y_line, color='red')
    plt.title(namegraph + " случай")
    plt.xlabel("Размер массива")
    plt.ylabel("Время работы функции")


def create_list(size, max_value, option):
    match option:
        case 'ordered':
            return list(range(1, size+1))
        case 'random':
            return [rnd.randint(1, max_value) for _ in range(size)]
        case 'reverse':
            return list(range(size, 0, -1))
        case _:
            return []


def func_time(class_func, case, case_name, size):
    time = []
    randmax = 1000000
    x = [i for i in range(10, 1001, 10)]
    repeat = 20
    for i in x:
        timer = 0
        for _ in range(repeat):
            list_temp = create_list(i, randmax, case[1])
            timer += (timeit.timeit(lambda: class_func.heap_sort(list_temp),
                                    number=1))
        time.append(timer/repeat)
    plt.figure(case[0] + case_name, size)
    plt.subplots_adjust(left=0.25)
    # Создание графиков
    create_graph(x, time, case[0])


if __name__ == '__main__':
    # Настройка размера окон
    dpi = 100
    width_inches = (1680 / dpi) / 4
    height_inches = (850 / dpi) / 2
    size = (width_inches, height_inches)
    item_func_name = {"Лучший": "ordered",
                      "Средний": "random", "Худший": "reverse"}
    for case_func in item_func_name.items():
        # func_time(x, heap_sort, case_func,
        #           " Пирамидальная сортировка", size)
        func_time(HeapqSort, case_func,
                  " Heapq сортировка", size)
        func_time(HeapSortSpeed, case_func,
                  " Heapq сортировка", size)

    # Показ графиков†
    plt.show()
