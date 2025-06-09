class Solution:
    def findWords(self, words):
        top_set = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
        mid_set = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
        bot_set = {"z", "x", "c", "v", "b", "n", "m"}
        res = []
        for word in words:
            curr_set = None
            letter = word[0].lower()  # find what set it could b in
            if letter in top_set:
                curr_set = top_set
            elif letter in mid_set:
                curr_set = mid_set
            elif letter in bot_set:
                curr_set = bot_set
            good_word = True
            for letter in word:
                letter = letter.lower()
                if letter not in curr_set:  # bad letter found
                    good_word = False
                    break
            if good_word:
                res.append(word)
        return res
