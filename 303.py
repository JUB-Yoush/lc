class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
        pass

    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix[right]
        l = self.prefix[left] if left > 0 else 0
        return r - l
        pass
