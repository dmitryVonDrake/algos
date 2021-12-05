def binary_search(lst, elem):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == elem:
            return mid
        if guess > elem:
            high = mid - 1
        else:
            low = mid + 1
    return None

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# low = 0, high = 9, mid = (0 + 9) // 2 = 4