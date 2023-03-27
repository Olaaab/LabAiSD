def lex_sort(nums):
    nums = [str(num) for num in nums]
    nums.sort()
    nums = [int(num) for num in nums]
    return nums

nums = [1, 2, 3, 11, 21, 111, 231]
sorted_nums = lex_sort(nums)
print(sorted_nums)