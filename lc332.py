#https://leetcode.com/problems/coin-change/description/
'''
question
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

so it's a dp question not a backtracking question
backtracking would make us generate every possible combonation to pay for the amount
they just want the one with the smallest array size ig
can't we just get the remainder of every value divided into the biggest coin?
repeat until remainder is 0
then return those values divided out or somthing
input isn't sorted
l test cases as usual leetcode
sorting is nlogn
and that would make the question pretty easy 
the challenge is trying to get it in n time
coins = [1, 6, 7, 9, 11] , amount = 13.
dp problem:
- what is the choice we keep making
- what influences that choice? (what is our goal in every choice)


'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: