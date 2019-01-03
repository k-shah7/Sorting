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

if __name__ == "__main__":
    data = [4, 3, 8, 9, 2, 4, 10]
    data2 = [8, 3, 1, 0, 4, 3, 1, 12, 6, 7]
    # print(heap_sort(data))
    trial = [4, 8, 9, 3, 2, 4]
    trial2 = [1, 9, 10, 4, 3, 2]
    print('Unsorted: ', data2)
    print(heap_sort(data2, True))
