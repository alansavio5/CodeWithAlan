# reduce() = apply a function to an iterable and reduce it to a single cumulative value,
#            performs the function on first two elements, and repeats the process until one value remains
#
# syntax >>>>> reduce(function,iterable)

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y:x+y,letters)     # iterating through letters and combining first two elements in that list until one element remains
print(word)

numbers = [1,2,3,4,5]
factorial = functools.reduce(lambda x,y:x*y,numbers)
print(factorial)
