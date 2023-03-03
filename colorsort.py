from typing import List
class Solution:
    def sortColors(self, nums: List[int]):
        left = count = 0
        right = len(nums)-1
        while count <= right:
            if nums[count] == 2:
                print(nums)
                nums[count], nums[right] = nums[right], nums[count]
                print(nums)
                right -= 1
            elif nums[count] == 0:
                nums[count], nums[left] = nums[left], nums[count]
                left += 1
                count += 1
            else:
                count += 1
        print("count:",count)
        return nums

solution = Solution()
print(solution.sortColors([2,0,2,1,1,0]))