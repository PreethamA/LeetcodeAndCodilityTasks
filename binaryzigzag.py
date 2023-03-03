"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
 (i.e., from left to right, then right to left for the next level and alternate between).
 Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
"""
from typing import List, Optional
from collections import deque
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(lst):
    n = len(lst)
    print(n)
    if n == 0:
        return None
    root = TreeNode(lst[0])
    if n > 1 and lst[1] is not None:
        root.left = buildTree(lst[1])
    if n > 2 and lst[2] is not None:
        root.right = buildTree(lst[2])
    return root


def zigzagLevelOrder(root):
    if not root or not hasattr(root, 'val') or not hasattr(root, 'left') or not hasattr(root, 'right'):
        return []

    levels = []
    queue = [root]
    left_to_right = True

    while queue:
        current_level = []
        for i in range(len(queue)):
            node = queue.pop(0)
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_to_right:
            current_level.reverse()
        levels.append(current_level)
        left_to_right = not left_to_right

    return levels

root = buildTree([3, 9, 20, 15, 7])
#sol = Solution()
#print(sol.zigzagLevelOrder([1,23,33,21,22,1,3]))
print(zigzagLevelOrder(root))