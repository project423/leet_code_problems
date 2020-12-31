# Leetcode practice problems

# Given a binary array, find the maximum number of consecutive 1s in this array.

# Input: [1,1,0,1,1,1]
# Output: 3
#1 NUMBER ONE
# nums = [1,1,1,0,1,1,1,1,1]
# # nums = [1,0,1,1,0,1]
# def findMaxConsecutiveOnes(nums):
#     count = max_count = 0
#     for num in nums:
#         if num == 1:
#             count += 1
#         else:
#             max_count = max(max_count, count)
#             count = 0
#     return max(max_count,count)
     

# print(findMaxConsecutiveOnes(nums))

#2 Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.
# nums = [12,345,2,6,789655,12]

# def findNumbers(n):
#     number_of_evens = 0
#     for n in nums:
#         count = 0
#         while n != 0:
#             n//= 10
#             count += 1
#         if count % 2 == 0:
#             number_of_evens += 1
#     return number_of_evens

# print(findNumbers(123))

#3 Squares of a Sorted Array
# nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# def sortedSquares(nums):
#     squared_list =  [num * num for num in nums]
#     squared_list.sort()
#     return squared_list
#     # return sorted(x*x for x in A)
# print(sortedSquares(nums))

# video walkthrough using pointers
# nums = [-10, -5, 1, 2, 4, 7]
# def sortedSquares(nums):
#     n = len(nums)
#     result = []
#     left_pointer = 0
#     right_pointer = n - 1
#     square = 0
#     for i in range(len(nums) - 1,-1,-1):
#         if(abs(nums[left_pointer]) < abs(nums[right_pointer])):
#             square = nums[right_pointer]
#             right_pointer -= 1
#         else:
#             square = nums[left_pointer]
#             left_pointer += 1
#         result.insert(0 , square * square)
#     return result

# print(sortedSquares(nums))
