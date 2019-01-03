test = [8, 7, 6, 5, 4, 3, 2, 1]


def insertion_sort(unsorted, verbose=False):
    """Sort a list using the Insertion sort algorithm.

    verbose - If true, prints passes
    """
    def order_list(working_list, insert_number):
        """Insert number into correct position in an ordered list."""
        for x, number in enumerate(working_list):
            if insert_number < number:
                working_list.insert(x, insert_number)
                break
        else:
            working_list.append(insert_number)

        return working_list

    working_list = [unsorted[0]]

    for insert_number in unsorted[1:]:
        if verbose:
            print(working_list, insert_number)

        working_list = order_list(working_list, insert_number)

    if verbose:
        print('Sorted List:', working_list)

    return working_list


print(insertion_sort(test, True))

assert insertion_sort(test) == sorted(test)
