# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# nums = [2, 7, 11, 15]
# target = 9
# def twoSum(nums, target):
#     prevMap = {} # val :index # creates a dictionary 
#     for i, n in enumerate(nums): #uses enumerate to add an index variable to each value in the array
#         diff = target - n  # 2 + n = 9 is equal to n = 9  - 2 so we are looking for if there is an 7 in the array
#         if diff in prevMap: #checks if 
#             return [prevMap[diff],i]
#         prevMap[n] = i # add a key value pair into the empy dictionary, first time is prevMap = {2:0}, then {2:0,7:1,}

# print(twoSum(nums,target))

# my_dict = {'one':1, 'two': 2}
# my_dict['three'] = 3
# print(my_dict)



nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
       
        
print(twoSum(nums,9))