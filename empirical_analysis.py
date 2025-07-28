import time
from part1_selection_algorithms import randomized_select, median_of_medians
import random

def test_algorithms():
    sizes = [100, 1000, 10000]
    for size in sizes:
        array = list(range(size))
        random.shuffle(array)
        k = size // 2

        print(f"\nArray size: {size}, k = {k}")

        start = time.time()
        rand_result = randomized_select(array[:], k)
        print(f"Randomized Select: {rand_result}, Time: {time.time() - start:.6f}s")

        start = time.time()
        det_result = median_of_medians(array[:], k)
        print(f"Deterministic Select: {det_result}, Time: {time.time() - start:.6f}s")

if __name__ == "__main__":
    test_algorithms()
