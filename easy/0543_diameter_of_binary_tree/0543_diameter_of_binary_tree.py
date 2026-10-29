# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.depth(root)
        return self.max_diameter

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth_left = self.depth(root.left)
        depth_right = self.depth(root.right)
        self.max_diameter = max(self.max_diameter, depth_left + depth_right)
        return max(depth_left, depth_right) + 1