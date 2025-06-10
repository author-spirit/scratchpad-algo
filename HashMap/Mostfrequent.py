def most_freq(nums):
    freq = {}

    for i in nums:
        if i % 2 != 0:
            continue

        freq[i] = freq.get(i, 0) + 1

    most_freq_num = -1
    for (num,count) in freq.items():
        prev_count = freq.get(most_freq_num, 0)
        if count > prev_count:
            most_freq_num = num

        # Tie, get minimum number
        if most_freq_num !=-1 and count == prev_count:
            most_freq_num = min(most_freq_num, num)

    return most_freq_num

nums = [29,47,21,41,13,37,25,7]
print(most_freq(nums))
