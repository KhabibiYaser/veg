from utils import *
from task1.src.merge_sort import *


def majority_delegate(array):
    n = len(array)
    if n == 0:
        return 0

    candidate = array[n // 2]
    count = 0

    for i in range(n):
        if array[i] == candidate:
            count += 1

    if count > n // 2:
        return 1
    return 0


def majority_delegate_main():
    n, arr = file_read_size_int_array()
    sorted_arr = merge_sort(arr)
    file_write([majority_delegate(sorted_arr)])


if __name__ == "__main__":
    majority_delegate_main()