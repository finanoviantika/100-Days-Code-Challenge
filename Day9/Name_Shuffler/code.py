'''
Link: https://www.codewars.com/kata/559ac78160f0be07c200005a/

Questions:

Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"

'''

def name_shuffler(str_):
    #your code here
    name = str_.split(" ")
    return name[1] + " " + name[0]