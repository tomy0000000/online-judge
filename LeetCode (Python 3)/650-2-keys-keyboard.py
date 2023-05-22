class Solution:
    def minSteps(self, n: int) -> int:
        
        if n == 1:
            return 0

        # Get divisors
        divisor = []
        for i in range(1, n+1):
            if n%i == 0:
                divisor.append(i)
        
        if len(divisor) == 2:
            # Prime number
            return n
        if len(divisor) % 2 == 0:
            # Most cases
            left = divisor[-2]
            right = divisor[1]
            return self.minSteps(left) + right
        else:
            # Perfect square
            middle = divisor[(len(divisor) - 1) // 2]
            return self.minSteps(middle) * 2
