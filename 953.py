"""
this smells like prefix trees, or a trie
the question is about sorting things lexographically, you use a trie for that
okay ignore tries, how could i solve this
there will always be a 26 char string for the order, we can map the position for free.
so we can look up any character and compare it's position
comparing every position to every other value would take a long time n^2
how to simplify comparisions?
caching?

solution:
if one word is a prefix of anohter, the smaller word wins
make map for char positions
loop over pairs of words
loop over chars
if we reach the end of w2 before the end of w1, w2 is a prefix of w1 and that's wrong
"""


class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_map = {}
        for i, c in enumerate(order):
            order_map[c] = i

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # loop over chars
            for j in range(len(w1)):
                if j == len(w2):  # prefix of w1
                    return False

                if w1[j] != w2[j]:
                    if order_map[w2[j]] < order_map[w1[j]]:  # w2 is earlier char, wrong
                        return False
                    break

        return False
