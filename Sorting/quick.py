def quick_sort(unsorted, verbose=False):
    """Sort list using Quick sort algorithm"""

    def partition_numbers(unsorted):
        """Choose pivot and partion numbers in list, with respect to the pivot.

        Numbers > pivot - moved to the right of the pivot
        Numbers < pivot - moved to the left of the pivot
        Pivot_list - True if number in list is pivot point
        """
        pivot_point = unsorted[0]
        # print("Pivot:", pivot_point, unsorted)
        # unsorted.remove(pivot_point) # why
        # oh true not needed!

        less_than = []
        more_than = []

        for number in unsorted[1:]:
            if number <= pivot_point:
                less_than.append(number)
            else:
                more_than.append(number)

        pivot_list_less = [False for number in less_than]
        pivot_list_more = [False for number in more_than]

        sorted_list = less_than + [pivot_point] + more_than

        pivot_list = pivot_list_less + [True] + pivot_list_more

        return sorted_list, pivot_list

    pivot_list = [False for number in unsorted]
    counter = 1

    while not all(pivot_list):

        start = pivot_list.index(False)
        if start + 1 == len(pivot_list):
            end = start + 1
        else:
            for end in range(start + 1, len(pivot_list)):
                if pivot_list[end] == True:
                    break
            else:
                end += 1

        working_list = unsorted[start:end]
        working_list = partition_numbers(working_list)

        unsorted[start:end] = working_list[0]
        pivot_list[start:end] = working_list[1]

        if verbose:
            print('Pass {}:'.format(counter), unsorted, pivot_list)

        counter += 1

    return unsorted




# test_1 = [2, 4, 5, 5, 4, 8, 2, 6]
# test_2 = [1, 1, 1, 1]
# test_3 = [6, 5, 4, 3, 2, 1, 0]
test_1 = [2, 6, 9, 3, 2, 7, 2, 1, 4, 6, 3]

assert quick_sort(test_1, True) == sorted(test_1)
# assert quick_sort(test_2, True) == sorted(test_2)
# assert quick_sort(test_3, True) == sorted(test_3)
