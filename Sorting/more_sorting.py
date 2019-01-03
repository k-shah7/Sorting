import random
import itertools


def is_sorted(test, view=False):
    for (i, item) in enumerate(test[1:]):
        if item < test[i]:
            return False
    return True


def bogosort_random(array):
    while not is_sorted(array):
        random.shuffle(array)

    return array


def bogosort_deterministic(array):
    for attempt in itertools.permutations(array):
        if is_sorted(attempt):
            return list(attempt)


def random_test(sort_function, cases=8, length=10):
    for _ in range(cases):
        case = random.sample(range(length), k=length)
        sort_case = sort_function(case)

        if not is_sorted(sort_case):
            print("Failure!\nFunction: {0}\nInput: {1} \nOutput {2}".format(
                sort_function.__name__, case, sort_case))
            return
    print("Passed!")


def quicksort_recursive(array):
    if len(array) <= 1:
        return array

    point = len(array) // 2

    pivot = array[point]
    left, right = [], []
    for i in array[:point]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    for i in array[point + 1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quicksort_recursive(left) + [pivot] + quicksort_recursive(right)


def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    j = high
    while True:
        while array[i] <= pivot and i <= j:
            i += 1
        while array[j] >= pivot and i <= j:
            j -= 1

        if j < i:
            break
        else:
            array[i], array[j] = array[j], array[i]
            print(array)

    array[low], array[j] = array[j], pivot


array = [5.5, 5, 1, 4, 9, 6, 3, 7, 8]
partition(array, 0, 8)
print(array)
