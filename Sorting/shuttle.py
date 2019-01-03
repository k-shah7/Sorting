# unsorted = [8, 3, 4, 2, 6, 5, 12, 100, 56, 78, 22, 12, 34]
test = [8, 3, 2, 6, 9, 4, 2, 7]


def shuttle(unsorted, verbose=False):
    """Sort a list using the shuttle sort algorithm.

    unsorted - the list to be sorted
    verbose - if True will print the passes
    """
    shuttle_range = len(unsorted) - 1
    for i in range(shuttle_range):
        x = i
        for number in range(i + 1):
            compare_1 = unsorted[x + 1]
            compare_2 = unsorted[x]
            if compare_1 > compare_2:
                break
            else:
                unsorted[x] = compare_1
                unsorted[x + 1] = compare_2
                x -= 1
        if verbose:
            print(unsorted)

    return unsorted


shuttle([8, 2, 4, 7, 1, 3])
shuttle(test, True)
# assert shuttle(test, False) == sorted(test)
