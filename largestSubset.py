def largestDivisibleSubset(nums):
    n = len(nums)

    if n == 0: return []

    nums.sort()

    dp = [[i] for i in nums]
    print(dp)
    for i in range(n):
        for j in range(i):
            print("I:",i)
            print("J:", j)
            print("Nums_i:",nums[i])
            print("Nums_j:", nums[j])
            if nums[i] % nums[j] == 0 :
                print("Read:",nums[i] % nums[j])
                dp[i] = dp[j] + [nums[i]]
                print("DP:",dp)
                #and len(dp[j]) + 1 > len(dp[i])
    return max(dp, key=len)

print(largestDivisibleSubset([1,3,5,6]))