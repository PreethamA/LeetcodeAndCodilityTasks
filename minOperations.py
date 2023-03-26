class Solution:
    def minOperations(self, n: int) -> int:
        cnt = 0
        while n:
            exp = 0
            while 2**exp < n:
                exp += 1
            print("Really:",exp)
            n = min(abs(2**exp - n), abs(2**(exp-1) - n))
            cnt += 1
        return cnt


s = Solution()
print(s.minOperations(32))