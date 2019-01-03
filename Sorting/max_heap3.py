test = [4, 5, 1, 2, 10, 12, 2, 2, 0]

def heap_sort(data):
    """Sort a list using the Heap Sort algorithm"""

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

    data = heapify(data)

    sorted_list = []

    for i in range(len(data)):
        sorted_list.insert(0, data[0])
        del data[0]
        data = heapify(data)

    return sorted_list


print(heap_sort(test))
