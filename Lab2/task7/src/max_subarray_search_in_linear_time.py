from utils import *


def kadane(array):
    if len(array) == 0:
        raise ValueError("Input array is empty.")

    max_so_far = max_ending_here = array[0]
    start = end = start_new = 0     # индексы для использования кода в задании 6

    for i in range(1, len(array)):
        if array[i] > max_ending_here + array[i]:
            max_ending_here = array[i]
            start_new = i
        else:
            max_ending_here += array[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = start_new
            end = i

    return start, end, max_so_far

def kadane_main():
    n, arr = file_read_size_int_array()
    start, end, max_subarray = kadane(arr)
    file_write([max_subarray])


if __name__ == '__main__':
    measure_performance(kadane_main)
