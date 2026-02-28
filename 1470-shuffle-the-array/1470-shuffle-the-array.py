class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arranged = []
        for i in range(n):
            arranged.append(nums[i])
            arranged.append(nums[i + n])

        return arranged