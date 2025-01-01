class Solution:
    def coinChange(self, coins, amount):
        mincoins = amount + 1

        def pickCoin(remaining,choices):
            nonlocal mincoins
            if remaining == 0:
                mincoins = min(mincoins,choices)
                return
            for coin in coins:
                if remaining - coin > -1:
                    pickCoin(remaining-coin,choices+1)

        pickCoin(amount,0)
        if mincoins == amount + 1:
            return -1
        return mincoins

print(Solution.coinChange(None,[1,2,5],11))