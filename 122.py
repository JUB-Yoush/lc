"""
when day i+1 > day i, you can make a profit.
you can end with or without owning a stock
track the change in value
for every day, calculate the total profit if sold on day afterwards
7,1,5,3,6,4
1,50,1,100
can't be greedy, need to buy and sell
dp? where is the repeated work?
cannot sell backwards, only compare from i+1 -> end
brute force:
for every day, iterate over remaining days and calculate the max profit
day:7,1,5,3,6,4
prf:0,5:4,1:4,3:4,0,0
need to make sure optimial sell days don't overlap
okay they'll always overlap because that's how numbers work

"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
