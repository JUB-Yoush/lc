class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def pick(i, picks):
            if sum(picks) == target:
                res.append(picks.copy())
            elif sum(picks) < target:
                if i < len(candidates):
                    picks.append(candidates[i])
                    pick(i, picks)
                    picks.pop()
                    pick(i + 1, picks)

        pick(target, [])
        return res
