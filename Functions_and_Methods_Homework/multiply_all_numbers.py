def multiply(nums):
    total = 1
    for num in nums:
        total *= num
    return total


print(multiply([1, 2, 3, -4]))
