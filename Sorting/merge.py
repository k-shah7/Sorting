def merge_sort(unsorted, verbose=False):
    """Sort a list using the merge sort algorithm.

    unsorted - List to be sorted
    verbose - If true then prints each pass
    """

    start_list = [[number] for number in unsorted]
    counter = 0

    while len(start_list) != 1:
        if len(start_list) % 2 == 1:
            start_list.append([])

        output_list = []

        for i in range(0, len(start_list), 2):
            left = start_list[i]
            right = start_list[i + 1]
            output_list.append(merge_lists(left, right))
        start_list = output_list

        if verbose:
            print('Pass:', counter + 1)
            print(start_list)

        counter += 1

    sorted_list = start_list[0]

    if verbose:
        print('Sorted List:', sorted_list)

    return sorted_list


# copied out for asserts
def merge_lists(left, right, verbose=False):
    """Merges two sorted lists together into one sorted list.
    verbose - If True will print each step"""
    output = []
    while left != [] and right != []:
        if left[0] < right[0]:
            output.append(left[0])
            left.remove(left[0])
            if verbose:
                print(output, left, right)

        else:
            output.append(right[0])
            right.remove(right[0])
            if verbose:
                print(output, left, right)

    if left == []:
        output.extend(right)
    else:
        output.extend(left)

    return output

def merge_sort2(unsorted, verbose=False):
    """Sort a list using the merge sort algorithm.

    unsorted - List to be sorted
    verbose - If true then prints each pass
    """

    start_list = [[number] for number in unsorted]
    counter = 0

    while len(start_list) != 1:

        output_list = []

        i = 0
        while i < len(start_list) - 1:
            left = start_list[i]
            right = start_list[i + 1]
            output_list.append(merge_lists(left, right))
            i += 2

        if i == len(start_list) - 1:
            output_list.append(start_list[i])
            # equivalently,
            # left = start_list[i]
            # output_list.append(merge_lists(left, []))

        start_list = output_list

        if verbose:
            print('Pass:', counter + 1)
            print(start_list)

        counter += 1

    sorted_list = start_list[0]

    if verbose:
        print('Sorted List:', sorted_list)

    return sorted_list

# unsorted = [3, 4, 8, 2, 6, 1, 9, 5, 7]
# print(merge_sort(unsorted, True))
# print(merge_lists([3, 5, 9], [1, 5, 7, 8], True))
# assert merge_sort(unsorted) == sorted(unsorted)
# assert len(merge_lists([0, 1, 10], [3, 5, 12])) == 6
# assert merge_lists([1, 2, 4], [3]) == [1, 2, 3, 4]
# assert merge_lists([], [],) == []
# assert merge_lists([], [1, 2, 3]) == [1, 2, 3]
# assert merge_lists([4, 6, 10], [1, 4, 11]) == [1, 4, 4, 6, 10, 11]
# assert merge_lists(["one", "two"], ["three"]) == ["one", "three", "two"]

print(merge_sort2([4, 2, 4, 3, 6, 1, 2], verbose=True))
