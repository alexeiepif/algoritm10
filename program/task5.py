import heapq
from random import randint


def print_sorted_sums(list1, list2):
    if not list1 or not list2:
        return

    list1.sort()
    list2.sort()

    heap = [(list1[0] + list2[0], 0, 0)]
    pushed = {(0, 0)}
    lenght = []

    for _ in range(len(list1) * len(list2)):
        lenght.append(len(heap))
        sum, i, j = heapq.heappop(heap)
        print(sum)
        if (i-1, j-1) in pushed:
            pushed.discard((i-1, j-1))
        else:
            pushed.discard((i, j))

        if i + 1 < len(list1) and (i + 1, j) not in pushed:
            heapq.heappush(heap, (list1[i + 1] + list2[j], i + 1, j))
            pushed.add((i + 1, j))

        if j + 1 < len(list2) and (i, j + 1) not in pushed:
            heapq.heappush(heap, (list1[i] + list2[j + 1], i, j + 1))
            pushed.add((i, j + 1))
    print(lenght)
    print(f'макс память - {max(lenght)}')


def summar(list1, list2):
    if not list1 or not list2:
        return

    sum = []
    for i in list1:
        for j in list2:
            sum.append(i+j)
    sum.sort()
    # print(sum)


def generate_random_list(len_list):
    random_list = [randint(0, 100
                           ) for _ in range(len_list)]
    return random_list

# list1 = [1, 3, 5, 7]
# list2 = [6, 7, 8, 9]
list1 = generate_random_list(10)
list2 = generate_random_list(10)
print_sorted_sums(list1, list2)
summar(list1, list2)
