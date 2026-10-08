# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p and q:
                return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            elif not p and not q:
                return True
            else:
                return False
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)