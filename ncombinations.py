def combine(n, k):
    def backtrack(first=1, pos=0):
        if pos == k:
            print('positons {} in res {}'.format(pos,combination[:]))
            res.append(combination[:])
            return
        for i in range(first, n + 1):
            combination[pos] = i
            print("combipostion:",combination[pos])
            print("combinations {} and position {}" .format(combination, pos))
            backtrack(i + 1, pos + 1)

    combination = [0] * k
    res = []
    backtrack()
    return res

print(combine(6,3))