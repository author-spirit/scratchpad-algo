class Solution():
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n= len(s)
        if not n:
            return 0
        min_string = ""
        max_string = ""
        l = -1
        r = 0
        freq = {}

        while l < r and r < n-1:
            next_string = s[r]
            if next_string not in freq:
                freq[next_string] = True
                min_string += next_string
            else:
                # reset frequency
                freq = {}
                l = r+1
            if len(min_string) > len(max_string):
                max_string = min_string
                min_string = ""
            r +=1 
        return max_string

sol = Solution()
print(sol.lengthOfLongestSubstring('pwwkew'))
