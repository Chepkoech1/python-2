#  Write a Python function to find the maximum sum of a subarray in a given
# list of integers

def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


print(max_subarray_sum([4,3,2,-9,8]))  
