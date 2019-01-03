class heap(object):

    def __init__(self, items=[]):
        self.heap = []
        for number in items:
            self.heap.append(number)

    def float_up(self, n):
        while (n + 1) // 2 >= 1:



    def __str__(self):
        return str(self.heap)

trial = heap([2, 1, 8, 4])

print(trial)
