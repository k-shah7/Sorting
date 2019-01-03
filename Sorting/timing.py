from max_heap3 import heap_sort
import random
import time

def testcase(size, number):
    total = 0

    for i in range(number):
        case = random.choices(range(size), k=size)

        start = time.time()
        heap_sort(case)
        end = time.time()

        total += end - start

    return total/number

def test_suite(number):
    samples = 50
    for i in range(samples):
        n = int(10**(1+i/samples*5))
        print(n, testcase(n, number), sep=',',flush=True)

if __name__ == "__main__":
    test_suite(10)
