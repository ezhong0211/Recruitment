class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 1
        else:
            return 1 + self.climbStairs(n - 1) + self.climbStairs(n - 2)
