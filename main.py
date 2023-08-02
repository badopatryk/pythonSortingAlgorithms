import time
import random
import matplotlib.pyplot as plt


def shell_sort(arr, n):
    gap = n//2

    while gap > 0:
        j = gap

        while j < n:
            i = j-gap

            while i >= 0:

                if arr[i+gap] > arr[i]:

                    break
                else:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]

                i = i-gap

            j += 1
        gap = gap//2


def partition(array, one, two):

    pivot = array[two]

    i = one - 1

    for j in range(one, two):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[two]) = (array[two], array[i + 1])

    return i + 1


def quick_sort(array, one, two):
    if one < two:

        pi = partition(array, one, two)

        quick_sort(array, one, pi - 1)

        quick_sort(array, pi + 1, two)


def counting_sort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radix_sort(array):
    max_element = max(array)

    place = 1
    while max_element // place > 0:
        counting_sort(array, place)
        place *= 10


def compare_sorting_algorithms_random_numbers(sizes):
    shell_sort_times = []
    quick_sort_times = []
    radix_sort_times = []
    for size in sizes:

        arr = [random.randint(0, 1000000) for _ in range(size)]
        start = time.time()
        shell_sort(arr, len(arr))
        shell_sort_times.append(time.time() - start)

        arr = [random.randint(0, 1000000) for _ in range(size)]
        start = time.time()
        quick_sort(arr, 0, len(arr)-1)
        quick_sort_times.append(time.time() - start)

        arr = [random.randint(0, 1000000) for _ in range(size)]
        start = time.time()
        radix_sort(arr)
        radix_sort_times.append(time.time() - start)

    plt.plot(sizes, shell_sort_times, label="Shell Sort")
    plt.plot(sizes, quick_sort_times, label="Quick Sort")
    plt.plot(sizes, radix_sort_times, label="Radix Sort")
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title("Comparison of Sorting Algorithms")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    sizes = [10, 100, 1000, 10000, 100000]
    compare_sorting_algorithms_random_numbers(sizes)
