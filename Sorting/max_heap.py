data = [4, 3, 8, 9, 2, 4, 10]


# def max_heapify(data, verbose=False):
#     """Turn list into a max heap"""

#     def maxify(data, parent):
#         """Ensure parent node is greater than child nodes"""
#         left = parent * 2 + 1
#         right = parent * 2 + 2

#         if data[parent] < data[left]:
#             data[parent], data[left] = data[left], data[parent]

#         elif data[parent] < data[right]:
#             data[parent], data[right] = data[right], data[parent]

#         return data

#     length = len(data) - 1
#     for i in range(length // 2, -1, -1):
#         maxify(data, i - 1)
#         if verbose:
#             print(data)

#     return data

# print(max_heapify(data, True))


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

def max_heapify(data):

    def bubble_up(data, child):
        """Move child node to correct place"""
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
            print('1', data)
            data, current_node, swap = result[0], result[1], result[2]
            # print(data, current_node, swap)
            if current_node == 0:
                return data

        return data

    print(bubble_up(data, 6))
    # start_index = len(data) - 1

    # while start_index != 0:
    return 'Hello'

print(max_heapify(data))
