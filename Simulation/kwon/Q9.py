# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축

# 1. 단순히 문자열이 압축되선 안되고, 예5번과 같이 제일 첫 문자부터 일정한 단어 갯수를 기준으로 압축 단위가 생성된다.
# 2. 최적화를 위해 압축된 문자열의 갯수를 세리는 방식은 반례가 생긴다.
# 2-1. 문자열이 압축이 되면 압축된 문자의 갯수를 (1 + 압축단위)로 세아렸는데, 이 경우 압축된 문자열의 갯수가
#      2자리 이상인 반례가 존재한다.
# 즉, 문자열 압축을 string을 통해서 직접 시뮬레이션해야한다.

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