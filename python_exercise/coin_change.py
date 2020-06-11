#dynamic programming
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combinations = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                combinations[i] += combinations[i-coin]
        return combinations[-1]


#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3353/