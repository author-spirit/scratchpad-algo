class Solution:
    def romanToInt(self, s: str) -> int:

        total = 0

        roman_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "!" : 0
        }

        skip_index = -1

        # curr
        for i in range(len(s)):

            if i == skip_index:
                continue;

            curr = s[i]
            curr_value = 0
            next_value = 0
            next = s[i+1] if i+1 < len(s) else "!"

            # if curr is greater than next then add to total
            if curr not in roman_map:
                continue;

            # get the actual value of roman number
            # Get the next actual value
            if next in roman_map:
                next_value = roman_map[next]

            # Get the curr index actual value
            if curr in roman_map:
                curr_value = roman_map[curr]

            # IF current value is greater than next value then just add current value to total
            if curr_value >= next_value:
                total = total + curr_value
            else:

                # Minus the curr value from next to get the actual number
                # e.g., IX = 4, I=1, X=5 then
                skip_index = i+1
                total = total + (next_value - curr_value)

        return total


sol = Solution()
result = sol.romanToInt("CD")
print(result)
