unsorted = [8, 3, 4, 2, 6, 5, 12, 100, 56, 78, 22, 12, 34]
try_list = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
test = [8, 3, 2, 6, 9, 4, 2, 7]


def bubble(unsorted):
    bubble_range = len(unsorted) - 1
    for x in range(bubble_range):
        changed = False
        for i in range(bubble_range - x):
            if unsorted[i] > unsorted[i + 1]:
                unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                changed = True

        print(unsorted)

        if not changed:
            break
    return unsorted

print(bubble(test))

# Best case: sorted list, therefore n - 1 comparisons have to be made O(n)
# Worst case: reverse order therefore (n-1) + (n-2) + (n-3) + ... + 1
# sum = 1/2(n - 1)(n) therefore O(n^2)
