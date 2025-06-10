class Solution:
    def hasDuplicate(self, nums) -> bool:
        items = {}
        for i in nums:
            if i not in items:
                items[i] = None
            else:
                return True
        return False
    
    def has_duplicates_xtd(self, nums):
        freq = {}
        if not nums:
            return False
        l = 0
        r = len(nums)-1
        while l <= r:
            left_num = nums[l]
            right_num = nums[r]
            if left_num in freq:
                return True
            freq[left_num] = True
            if right_num in freq:
                return True
            freq[right_num] = True
            l += 1
            r -= 1
        return False
    
    def has_duplicates_fast(self, nums):
        if not nums: return False
        return len(set(nums)) != len(nums)

sol = Solution()
print(sol.has_duplicates_fast([8,5,8,3,7,12]))
