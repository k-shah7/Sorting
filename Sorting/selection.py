test = [1, 2, 1, 1, 1, 1, 1]
# coding style is really coming along, good work!
# => :) :) just copying coding style :P
# : haha awww :)


def selection_sort(unsorted, verbose=False):
    """Sort a list using the selection sort algorithm.

    verbose - If true, prints passes
    """
    def swap_min(unsorted):
        """Find smallest number in list and swap with first number."""
        current_min = unsorted[0]
        x = 0
        for i, number in enumerate(unsorted):
            if number < current_min:
                current_min = number
                x = i

        unsorted[0], unsorted[x] = current_min, unsorted[0]

    for i in range(len(unsorted) - 1):

        working_list = unsorted[i:]

        swap_min(working_list)
        unsorted = unsorted[:i] + working_list

        if verbose:
            print('Pass {}:'.format(i + 1), unsorted)

    return unsorted


def selection_sort2(unsorted, verbose=False):
    """Sort a list using the selection sort algorithm.

    verbose - If true, prints passes
    """
    for i in range(len(unsorted) - 1):

        current_min = unsorted[i]
        x = i
        for z, number in enumerate(unsorted[i:], i):
            if number < current_min:
                current_min = number
                x = z

        unsorted[i], unsorted[x] = current_min, unsorted[i]

        if verbose:
            print('Pass {}:'.format(i + 1), unsorted)

    return unsorted

print(selection_sort2([2, 5, 1, 4, 9, 6, 3, 7, 8], True))
