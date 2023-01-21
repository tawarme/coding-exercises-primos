class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amt = [amount + 1 for i in range(amount+1)]

        amt[0] = 0

        for i in range(1, amount+1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    amt[i] = min(amt[i], 1 + amt[i - coins[j]])

        if amt[amount] > amount:
            return -1
        return amt[amount]
        
