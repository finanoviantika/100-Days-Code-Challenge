'''
Link: https://www.codewars.com/kata/555086d53eac039a2a000083/

Questions:

Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

'''

def lovefunc( flower1, flower2 ):
    # ...
    if (flower1 % 2 or flower2 % 2) == 0 and (flower1 % 2 or flower2 % 2) == 0:
        return False
    if (flower1 % 1 and flower2 % 1) == 1 and (flower1 % 1 and flower2 % 1) == 1:
        return False
    if (flower1 % 2 or flower2 % 2) == 0 or (flower1 % 1 or flower2 % 1) == 1:
        return True
    if (flower1 % 1 and flower2 % 1) == 1 or (flower1 % 2 and flower2 % 2) == 0:
        return True
    else:
        return False