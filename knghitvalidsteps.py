from typing import List
from collections import defaultdict
from math import prod


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        diff = [
            [2, 1],
            [1, 2],
        ]
        # based on the grid value saving the Row,Col in dictionary
        # key : [Value]  ::: Grid_Number : [row,column]
        new = defaultdict(list)
        n = len(grid)
        print(new)
        print(f'grid length:{n}')
        for i in range(n):
            for j in range(n):
                new[grid[i][j]].append(i)
                new[grid[i][j]].append(j)
                print(i)
        print(new)
        # Must check condition Grid need to start at left top
        # A specific testcase is given to check this.
        if new[0] != [0, 0]:
            return False

        # Remaining just check if the absolute diff of Row & Col
        # is within the range, i.e, [1,2] or [2,1]
        # If not Return False
        for i in range((n * n) - 1):
            #print("value1:",new[i][0])
            #print("value2:",new[i + 1][0])
            row = abs(new[i][0] - new[i + 1][0])
            col = abs(new[i][1] - new[i + 1][1])

            if [row, col] not in diff:
                return False

        # If Everything is perfect return True
        return True


grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
sol = Solution()
print(sol.checkValidGrid(grid))