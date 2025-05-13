class Solution:
    def coinChange(self, coins, amount):
        mincoins = amount + 1
        cache = {}

        def pickCoin(remaining, choices) -> int:
            nonlocal mincoins
            if (remaining, choices) in cache:
                return cache[(remaining, choices)]

            if remaining == 0:
                mincoins = min(mincoins, choices)
                cache[(remaining, choices)] = mincoins
                return cache[(remaining, choices)]

            for coin in coins:
                if remaining - coin > -1 and choices < mincoins:
                    cache[(remaining, choices)] = (
                        pickCoin(remaining - coin, choices + 1) + 1
                    )
            return cache[(remaining, choices)]

        pickCoin(amount, 0)
        if mincoins == amount + 1:
            return -1
        return cache[(amount, 0)]


print(Solution.coinChange(None, [1, 2, 5], 11))

