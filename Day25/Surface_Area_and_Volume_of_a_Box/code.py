'''
Link: https://www.codewars.com/kata/565f5825379664a26b00007c/

Quetions:

Write a function that returns the total surface area and volume of a box as an array: [area, volume]

'''

def get_size(w,h,d):
    #your code here
    area = 2*(h*w) + 2*(h*d) + 2*(w*d)
    volume = w*h*d
    return [area, volume]