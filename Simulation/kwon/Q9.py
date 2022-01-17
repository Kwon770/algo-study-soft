def solution(s):
    ans = 987654321
    for size in range(1, len(s)//2 + 1):

        localAns = 0
        idx = 0
        isEndStep = False
        while idx < len(s):

            zipStep = 1
            isZipped = True
            while isZipped:
                if idx + (zipStep+1) * size > len(s):
                    isZipped = False
                    isEndStep = True
                    break;

                if s[idx:idx + size] != s[idx + zipStep * size:idx + (zipStep+1) * size]:
                    isZipped = False
                    break;

                zipStep += 1

            if zipStep > 1:
                localAns += 1+size
                idx += zipStep * size
            else:
                if isEndStep:
                    localAns += len(s[idx:])
                    break
                else:
                    localAns += size
                    idx += size

        if ans > localAns:
            ans = localAns

    return ans
