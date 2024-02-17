'''
Link: https://www.codewars.com/kata/56b29582461215098d00000f/

The pipes connecting your level's stages together need to be fixed before you receive any more complaints.

The pipes are correct when each pipe after the first is 1 more than the previous one.

Task
Given a list of unique numbers sorted in ascending order, return a new list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).

Example
Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8

'''

def pipe_fix(nums):
    min_ = min(nums)
    max_ = max(nums)
    
    return list(range(min_, max_+1))