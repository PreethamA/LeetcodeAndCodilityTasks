from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=list(set(nums))
        print(k)
        l={i:nums.count(i) for i in k}
        print(l)
        for i in k:
            if(l[i]>2):

                print("l[i]-2",l[i])
                for j in range(l[i]-2):
                    print("j",j)
                    nums.remove(i)
        return len(nums)


solution = Solution()
print(solution.removeDuplicates([1,1,1,2,2,3,3,3,5,5,5,5]))