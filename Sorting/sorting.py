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


def bubble(unsorted, verbose=False):
    """Sort a list using the shuttle sort algorithm.

    unsorted - the list to be sorted
    verbose - if True will print the passes
    """
    bubble_range = len(unsorted) - 1
    for x in range(bubble_range):
        changed = False
        for i in range(bubble_range - x):
            if unsorted[i] > unsorted[i + 1]:
                unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                changed = True

        if verbose:
            print(unsorted)

        if not changed:
            break
    return unsorted


def merge_sort(unsorted, verbose=False):
    """Sort a list using the merge sort algorithm.

    unsorted - List to be sorted
    verbose - If true then prints each pass
    """

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


def merge_sort2(unsorted, verbose=False):
    """Sort a list using the merge sort algorithm.

    unsorted - List to be sorted
    verbose - If true then prints each pass
    """
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


def heap_sort(data, verbose=False):
    """Sort a list using the Heap Sort algorithm
    verbose - If True, prints passes
    """

    def heapify(data):
        """Make a list into a max heap"""

        def bubble_up(data, child):
            """Move child to correct position in heap"""

            def swap_parent(data, child):
                """Swap values if parent greater than child.
                Return data list and index of the child after swap"""

                parent = ((child + 1) // 2) - 1

                if data[parent] < data[child]:
                    data[parent], data[child] = data[child], data[parent]
                    child_index = parent
                    swap = True
                else:
                    child_index = child
                    swap = False

                return data, child_index, swap

            current_node = child
            swap = True
            while swap:
                result = swap_parent(data, current_node)
                data, current_node, swap = result[0], result[1], result[2]
                # print(data, current_node, swap)
                if current_node == 0:
                    return data

            return data

        for i in range(len(data)):
            bubble_up(data, i)

        return data

    def bubble_down(data):
        """Move head to correct position in heap"""
        def swap_child(data, parent_index):
            """Swap values if parent is less than children"""
            max_index = len(data) - 1
            child1_index = (parent_index + 1) * 2 - 1
            child2_index = (parent_index + 1) * 2
            # print(number)

            if child1_index and child2_index <= max_index:
                child1, child2 = data[child1_index], data[child2_index]

                if child1 > child2:
                    compare_index = child1_index

                else:
                    compare_index = child2_index

            elif child1_index <= max_index and child2_index > max_index:
                compare_index = child1_index

            else:
                swap = False
                return data, parent_index, swap

            if data[parent_index] < data[compare_index]:
                data[parent_index], data[compare_index] = data[compare_index], data[parent_index]
                swap = True
                parent_index = compare_index
                return data, parent_index, swap

            else:
                swap = False
                return data, parent_index, swap

        max_index = len(data) - 1
        current_node = 0
        swap = True
        while swap:
            result = swap_child(data, current_node)
            data, current_node, swap = result[0], result[1], result[2]
            if current_node == max_index:
                return data

        return data

    def swap_ends(data, swap_index):
        data[0], data[swap_index] = data[swap_index], data[0]
        return data

    data = heapify(data)

    if verbose:
        print('heap: ', data)

    length = len(data) - 1

    for i in range(length):
        data = swap_ends(data, length - i)

        if verbose:
            print('swapped: ', data)

        data[0:length - i] = bubble_down(data[0:length - i])

        if verbose:
            print('heaped: ', data)

    return data


def quick_sort(unsorted, verbose=False):
    """Sort list using Quick sort algorithm"""

    def partition_numbers(unsorted):
        """Choose pivot and partion numbers in list, with respect to the pivot.

        Numbers > pivot - moved to the right of the pivot
        Numbers < pivot - moved to the left of the pivot
        Pivot_list - True if number in list is pivot point
        """
        pivot_point = unsorted[0]
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
