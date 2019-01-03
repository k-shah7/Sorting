test = [3, 6, 8, 4, 5, 2, 1]


def insertion_sort(unsorted, verbose=False):
    """Sort a list using the Insertion sort algorithm.

    verbose - If true, prints passes
    """
    def order_list(working_list, insert_number):
        """Inserts number into correct position in an ordered list."""

        x = 1

        while insert_number < working_list[-x]:
            # i'm not entirely convinced a while loop is the best loop here
            # for x in range(1, len(working_list)) maybe?
            # also look at enumerate in the tutorial thing i sent
            x += 1

            if x > len(working_list):
                break

        insert_position = len(working_list) - (x - 1)
        working_list.insert(insert_position, insert_number)

        ordered_list = working_list  # what's the point of the rename

        return ordered_list

    working_list = unsorted[:1]  # is the slice really necessary

    # for i in range(len(unsorted) - 1):  # maybe not the best loop
    #     # again look at enumerate
    #     insert_number = unsorted[i + 1]

    #     if verbose:
    #         print('Pass {}:'.format(i + 1), working_list, insert_number)

    #     working_list = order_list(working_list, insert_number)

    for (i, insert_number) in enumerate(unsorted[1:], 1):
        # again look at enumerate
        if verbose:
            print('Pass {}:'.format(i), working_list, insert_number)

        working_list = order_list(working_list, insert_number)

    sorted_list = working_list  #

    if verbose:
        print('Sorted List:', sorted_list)

    return sorted_list


print(insertion_sort(test, True))
assert insertion_sort(test) == sorted(test)
