def count(array, target):
    n = len(array)

    a = first_search(array, target, 0, n - 1)

    if a == None:
        return -1
    b = last_search(array, target, 0, n - 1)

    return b - a + 1


def first_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first_search(array, target, start, mid - 1)
    else:
        return first_search(array, target, mid + 1, end)


def last_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last_search(array, target, start, mid - 1)
    else:
        return last_search(array, target, mid + 1, end)


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = count(array, target)
print(result)