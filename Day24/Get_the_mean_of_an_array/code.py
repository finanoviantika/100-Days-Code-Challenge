'''
Link: https://www.codewars.com/kata/563e320cee5dddcf77000158/

Questions:

It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.

'''

from statistics import mean
import math

def get_average(marks):
    return math.floor(mean(marks))