import random
def exists(numbers, num):
    """
    returns True if "num" exists in list "numbers" otherwise False
    """
    return num in numbers

def distinct_random_numbers(min, max, size):
    """
    returns list with "size" distinct random numbers 
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    requirement: to use the above function "exists" and one while-loop
    """
    if (max - min + 1) < size:
        return []   
    result = []
    while len(result) < size:
        num = random.randint(min, max)
        if not exists(result, num):
            result.append(num)
            
    return result
print (distinct_random_numbers(1, 49, 7)) 

""" Part 1 is left as is because a while-loop is
necessary to handle random duplicates. List comprehension doesn't work for this logic """

