class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        while pow(2, power) <= n:
            if pow(2, power) == n:
                return True
            power += 1
        return False

answer = Solution().isPowerOfTwo(3)
print(answer)