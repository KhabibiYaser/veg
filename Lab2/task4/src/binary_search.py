from utils import *


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_main():
    with open('../txtf/input.txt', 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
        k = int(file.readline().strip())
        b = list(map(int, file.readline().strip().split()))

    results = []
    for target in b:
        index = binary_search(arr, target)
        results.append(index)

    file_write(results)
    return arr, b

if __name__ == '__main__':
    measure_performance(binary_search_main)
