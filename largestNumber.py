from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = []
        for num in nums:
            str_nums.append(str(num))  # turn numbers to strings

        str_nums.sort(reverse=True)  # sort by lexicographical order
        print(str_nums)
        '''
        flag = False  # flag to keep track if there were swaps, if no more swaps needed - finished
        while not flag:
            flag = True
            i = 0
            while i < len(str_nums) - 1:
                if str_nums[i] + str_nums[i + 1] < str_nums[i + 1] + str_nums[i]:  # if larger when swapped - swap
                    str_nums[i], str_nums[i + 1] = str_nums[i + 1], str_nums[i]
                    print(str_nums)
                    flag = False
                i += 1
        '''
        res = "".join(str_nums)

        if res[0] == '0':
            return str(0)

        return res

def largestNumber( nums: List[int]) -> str:
    str_nums = []


    nums.sort(reverse=True)  # sort by lexicographical order
    print(nums)
    return "".join(map(str,nums))
sol = Solution()
print(sol.largestNumber([0,1,1,4,4,6]))
print(largestNumber([0,1,1,4,4,6]))