class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        l,r = 0,len(nums)-1
        while l <= r:
            m = math.floor((l+r)/2)
            if nums[m] == target:
                index = m
                return index
            elif target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
        return index
