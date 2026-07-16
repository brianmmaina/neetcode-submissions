class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node):
            if not node or len(res) >= k:
                return
            dfs(node.left)
            if len(res) < k:
                res.append(node.val)
            dfs(node.right)  
        dfs(root)
        return res[k-1]