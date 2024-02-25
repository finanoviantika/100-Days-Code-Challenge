'''
Link: https://www.codewars.com/kata/5715eaedb436cf5606000381/train/

Questions:

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.

'''

def positive_sum(arr):
    # Your code here
    nu = []
    
    for num in arr:
        if num > 0:
            nu.append(num)
    return sum(nu)
