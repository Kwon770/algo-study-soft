def solution(s):
    answer = len(s)
    for size in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:size]
        count = 1

        for i in range(size, len(s), size):
            cur = s[i:i + size]

            if prev == cur:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = cur
                count = 1

        compressed += str(count) + prev if count > 1 else prev
        answer = min(answer, len(compressed))

    return answer