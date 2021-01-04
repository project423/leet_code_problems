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


#3 Duplicate Zeros
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# nums = [1,0,2,3,0,4,5,0]


# def duplicateZeros(nums):
#     for i in range(len(nums) - 1, -1 ,-1):
#         if nums[i] == 0:
#             print(i)
#             nums.pop()
#             nums.insert(i,0)
    
    
    

# print(duplicateZeros(nums))

#4 Check If N and Its Double Exist
# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
# arr = [10,2,5,3]
# arr = [7,1,14,11]
# arr = [3,1,7,11]
# arr = [-2,0,10,-19,4,6,-8]
# arr = [-20,8,-6,-14,0,-19,14,4]
# arr = [3,1,7,11]
#My solution
# def checkIfExist(arr):
#     if arr.count(0) ==2: return True
#     for i in range(len(arr)):
#         for num in arr:
#             if arr[i] * 2 == num and arr[i] != num:           
#                 return True
#     return False
 #Better solution

# def checkIfExist(arr):
#     seen = set()
#     for i in arr:
#         if 2 * i in seen or i / 2 in seen:
#             return True
#         seen.add(i)
#     return False



# print(checkIfExist([-2,0,10,-19,4,6,-8])) #false
# print(checkIfExist([-20,8,-6,-14,0,-19,14,4])) #true
# print(checkIfExist([0,0])) #true
# print(checkIfExist([2,3,3,0,0])) #true
# print(checkIfExist([11,2,8,3,3,0,16])) #true
    