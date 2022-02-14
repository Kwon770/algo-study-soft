# https://programmers.co.kr/learn/courses/30/lessons/60060

# 확인할 가사의 대상을 이진탐색을 활용하여 줄였지만, 여전히 선형탐색을 이용하기 때문에 시간초과
# 풀이에 트라이를 이용하거나, 일치하는 가사의 갯수를 이진탐색을 통해 계산해야 한다.

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