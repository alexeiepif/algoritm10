import heapq

def print_sorted_sums(arr1, arr2):
    if not arr1 or not arr2:
        return  

    arr1.sort()
    arr2.sort()

    heap = [(arr1[0] + arr2[0], 0, 0)]
    pushed = {(0, 0)}

    for _ in range(len(arr1) * len(arr2)):
        sum, i, j = heapq.heappop(heap)
        print(sum) 

        if i + 1 < len(arr1) and (i + 1, j) not in pushed:
            heapq.heappush(heap, (arr1[i + 1] + arr2[j], i + 1, j))
            pushed.add((i + 1, j))

        if j + 1 < len(arr2) and (i, j + 1) not in pushed:
            heapq.heappush(heap, (arr1[i] + arr2[j + 1], i, j + 1))
            pushed.add((i, j + 1))

# Пример использования функции:
arr1 = [4,3,13,2,2,3,45,67,8,2]
arr2 = [3, 5,34,4,4,5,67,8,6,4]
print_sorted_sums(arr1, arr2)
