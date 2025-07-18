"""
returning number of words, not the words themselves
we need to form a graph of all the words, and then perform a bfs over them. the shortest path is the correct one and we return it's len
form graph:
    if chars differeing == 1 then they're connected to each other
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        def chars_differing(a: str, b: str) -> bool:
            return len(set(a) & set(b)) == len(a) - 1

        # form graph
        adj_list = {}
        wordList.append(beginWord)
        for word in wordList:
            adj_list[word] = []

        for i in range(len(wordList)):
            for j in range(i, len(wordList)):
                a = wordList[i]
                b = wordList[j]
                if a != b and chars_differing(a, b):
                    adj_list[a].append(b)
                    adj_list[b].append(a)

        # bfs
        time = 0
        record = 5001
        queue = []
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        while queue:
            curr_word = queue.pop()
            for word in adj_list[curr_word]:
                if word == endWord:
                    record = min(time, record)
                if word not in visited:
                    queue.append(word)
                    visited.add(word)
            time += 1

        if record == 5001:
            return 0
        return time


# print(len(set("hot") & set("lot")) == len("hot") - 1)

print(
    Solution.ladderLength(
        None, "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    )
)
