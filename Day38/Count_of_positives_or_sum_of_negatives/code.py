'''
Link: https://www.codewars.com/kata/576bb71bbbcf0951d5000044/

Questions: 

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

'''

def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return []
    
    num_positive = num_negative = 0
    for num in arr:
        if num > 0:
            num_positive += 1
        elif num < 0:
            num_negative += num
    return [num_positive, num_negative]