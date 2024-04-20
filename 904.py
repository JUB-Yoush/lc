# https://leetcode.com/problems/fruit-into-baskets/
'''
- you can only collect two kinds of fruit
- each tree can have a unique fruit
- you need to pick a fruit from every tree while moving to the right
- you don't wrap around once you reach n tree
- you must stop when you can't pick a fruit
- the decision is where to start
- everything else is just simulation
- bf: start at every tree and calculate the max fruit count of each (n^2)
- what influences the decision of where to start
- which one has the largest subset of only 2 values?
- use a set to maintain the fruits in our collection
- also maintain the size of the subset
- record where the subset starts, and where it ends + the higest one
- return the higest one
'''

# sets don't work good, I'd need to track all occurances of a tree and not just the one
# I don't track the fruits in between l and r, and I don't want to loop through all of them to check cuz n^2


class Solution:
    def totalFruit(self, fruits) -> int:
        fruit_types = set()
        longest_line = (0,0)
        l,r= 0,0
        while r < len(fruits):
            # if good fruit type
            if fruits[r] not in fruit_types:
                fruit_types.add(fruits[r])
            if len(fruit_types) > 2:
                while len(fruit_types) > 2:
                    fruit_types.remove(fruits[l])
                    l+= 1
                    fruit_types.add(fruits[l])
                r+=1
            else:
                if (r+1 - l) > longest_line[1]:
                    longest_line = (l,r+1-l)
                r+= 1

        return longest_line[1]



class Solution:
    def totalFruit(self, fruits) -> int:
        count = collections.defaultdict(int)
        l,total,res = 0,0,0
        for r in range(len(fruits)):
            count[fruits[r]] += 
            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1
                l += 1
                if not count[f]:
                    count.pop(f)
            res = max(res,total)
        return res

print(Solution.totalFruit(None,[3,3,3,1,2,1,1,2,3,3,4])) #5