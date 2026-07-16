# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            #collecting boolean and height
            if not root: return [True, 0]

            #calling dfs on subtrees
            left, right = dfs(root.left), dfs(root.right)

            #checking if it is balanced in the subtree, Has to be true and the value heights are balanced
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            #returning if it's balanced and the height of the tree
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
        