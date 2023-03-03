from typing import List
def searchMatrix(matrix:List[List[int]], target: int):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m*n-1

    while left <= right:
        mid = left + (right-left)//2
        row = mid//n
        col = mid%n


        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            left = mid+1
        else:
            right = mid-1
    return False

print(searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]],target=6))