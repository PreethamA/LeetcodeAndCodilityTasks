def subsets(nums):
    def backtrack(first=0, pos=0):
        print(subset[:pos])
        res.append(subset[:pos])
        for i in range(first, len(nums)):
            subset[pos] = nums[i]
            backtrack(i + 1, pos + 1)

    subset = [None] * len(nums)
    res = []
    backtrack()
    return res

print(subsets([1,3]))