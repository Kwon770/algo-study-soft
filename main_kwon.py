# https://www.acmicpc.net/problem/2110
# 2110 공유기 설치
# Memory : 40656 KB, Time : 308 ms

# 이분 탐색을 적용하지 않으면 시간 초과가 나는 문제
# 최적화 포인트는
# 1. 가능한 거리를 확인할 때 high 를 최대값을 설정하는 것이 아니라, 실질적으로 가능한 값의 최대로 설정 (집 간의 총 거리 // (공유기 수-1) + 1)
# 2. 해당 거리를 둔 설치가 가능한지 확인할 때, 단순히 모든 집을 돌면서 확인하는게 아니라 여기서도 이분 탐색을 활용

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline


def solution(words, queries):
    sorted_words = sorted([(len(word), word) for word in words])
    bs_lengths, bs_words = zip(*sorted_words)
    answer = []

    for query in queries:
        sorted_query = sorted([(q, idx) for idx, q in enumerate(query)])
        bs_query, bs_index = zip(*sorted_query)

        cnt = 0
        query_len = len(query)

        wild_left = bs_index[bisect_left(bs_query, '?')]
        wild_right = bs_index[bisect_right(bs_query, '?') - 1]
        word_bs_left = bisect_left(bs_lengths, query_len)
        word_bs_right = bisect_right(bs_lengths, query_len)
        if wild_left == 0 and wild_right == query_len:
            answer.append(word_bs_right - word_bs_left + 1)
        else:
            for i in range(word_bs_left, word_bs_right):
                target = bs_words[i]
                if wild_left == 0 and target[wild_right + 1:] == query[wild_right + 1:]:
                    cnt += 1
                elif wild_left != 0 and target[:wild_left] == query[:wild_left]:
                    cnt += 1

            answer.append(cnt)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))