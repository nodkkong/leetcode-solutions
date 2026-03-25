class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        for i in range(2, n):
            next = a + b
            a = b
            b = next

        return b