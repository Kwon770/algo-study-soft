import sys

n, c = map(int, sys.stdin.readline().split())
array=[int(sys.stdin.readline()) for _ in range(n)]

array.sort()

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in array:
            if i >= current + mid:
                count += 1
                current = i

        if count >= c:
            start = mid + 1
            global answer
            answer = mid
        else:
            end = mid - 1


start = 1
end = array[n-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)