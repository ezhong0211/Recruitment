# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        print(root)
        dp = {}  # root -> total path sum to that root

        def solve_dp(root, dp):
            if root == None:
                dp[root] = 0
                return 0
            if root not in dp:
                left = root.left
                right = root.right
                maximum = max(
                    solve_dp(left, dp),
                    solve_dp(right, dp),
                    solve_dp(left, dp) + solve_dp(right, dp) + root.val,
                )
                dp[root] = (
                    maximum
                    if maximum != 0
                    else solve_dp(left) + solve_dp(right) + root.val
                )
            else:
                return dp[root]

        solve_dp(root, dp)
        return dp[root]
