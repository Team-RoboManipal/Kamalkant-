def longest_increasing_subsequence_length(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n 
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


input_list = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence_length(input_list))
