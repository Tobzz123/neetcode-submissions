class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set(nums)
        print(uniques)
        print(nums)
        print(len(nums))
        print(len(uniques))
        return len(nums) != len(uniques)
        