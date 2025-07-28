import random

def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    def chunks(lst, size):
        return [lst[i:i + size] for i in range(0, len(lst), size)]

    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks(arr, 5)]
    pivot = median_of_medians(medians, len(medians)//2)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))


def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return randomized_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))
