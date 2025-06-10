# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# My Leetcode solution:
https://leetcode.com/problems/first-bad-version/solutions/6739130/python-isbadversion-api-takes-care-of-ve-o9ie

def isBadVersion(n):
    bad = 1
    return n >= bad

class Solution:    
    def firstBadVersion(self, n):
        low = 1
        high = n
        val = -1
        while low <= high:
            mid = int(low+(high-low)/2)
            # Any higher version will be eventually reduced
            if isBadVersion(mid):
                val = mid
                high = mid -1
            else:
                low = mid+1

        return val

sol = Solution()
print(sol.firstBadVersion(1))
