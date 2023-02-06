class Solution:
    def race(self, target, dp):

        if dp[target] >= 0:
            return dp[target]
        
        dp[target] = float("inf")

        x = 1
        j = 1

        while j < target:

            p = 0
            q = 0
            while p < j:

                dp[target] = min(dp[target], x + 1 + 1 + q + self.race(target - (j - p), dp))

                q += 1
                p = (1 << q ) - 1

            x += 1
            j = (1 << x) - 1

        dp[target] = min(dp[target], x + ((1 + self.race(j - target, dp)) if target != j else 0))
        
        return dp[target]


    def racecar(self, target: int) -> int:

        dp = [-1 for i in range(target + 1)]

        dp[0] = 0

        #self.race(target, dp)

        return self.race(target, dp)


