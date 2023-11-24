#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import timeit
from scipy.optimize import curve_fit
import heapq


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
        work_list[i], work_list[largest] = work_list[largest], work_list[i]  # Свап

        # Применить heapify к корню
        heapify(work_list, n, largest)


def heap_sort(li):
    work_list = li.copy()
    n = len(work_list)

    # Построение максимальной кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(work_list, n, i)

    # Отдельное извлечение элементов из кучи
    for i in range(n-1, 0, -1):
        work_list[i], work_list[0] = work_list[0], work_list[i]  # Свап
        heapify(work_list, i, 0)

    return work_list


def heap_sort_py(iterable):
    # Преобразование списка в кучу
    heapq.heapify(iterable)

    # Извлечение минимальных элементов из кучи для сортировки
    return [heapq.heappop(iterable) for _ in range(len(iterable))]


def find_coeffs_bin(x, time):
    params, covariance = curve_fit(n_log_n, np.array(x),
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


def func_time(x, model, case, case_name, size):
    time = []
    randmax = 1000000
    for i in x:
        timer = 0
        for _ in range(50):
            list_temp = create_list(i, randmax, case[1])
            timer += (timeit.timeit(lambda: model(list_temp),
                                    number=1))
        time.append(timer/50)

    plt.figure(case[0] + case_name, size)
    plt.subplots_adjust(left=0.25)
    # Создание графиков
    create_graph(x, time, case[0])


if __name__ == '__main__':
    x = [i for i in range(10, 501, 10)]
    # Настройка размера окон
    dpi = 100
    width_inches = (1680 / dpi) / 4
    height_inches = (850 / dpi) / 2
    size = (width_inches, height_inches)
    item_func_name = {"Лучший": "ordered",
                      "Средний": "random", "Худший": "reverse"}
    for case_func in item_func_name.items():
        func_time(x, heap_sort, case_func,
                  " Пирамидальная сортировка", size)
        func_time(x, heap_sort_py, case_func,
                  " Heapq сортировка", size)

    # Показ графиков†
    plt.show()
