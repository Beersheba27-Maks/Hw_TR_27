import random
def exists(numbers, num):

    return num in numbers

def distinct_random_numbers(min, max, size):

    if (max - min + 1) < size:
        return []   
    result = []
    while len(result) < size:
        num = random.randint(min, max)
        if not exists(result, num):
            result.append(num)
            
    return result
print (distinct_random_numbers(1, 49, 7)) 

# 1. list
generated_numbers = distinct_random_numbers(1, 49, 7)
print("Original:", generated_numbers)
reversed_list = generated_numbers[::-1]
print("Reversed:", reversed_list)

# 2. Slicing
first_4 = generated_numbers[0:4]
reversed_list_4 = first_4[::-1]
print("first 4:", first_4)
print("reversed:", reversed_list_4)

# 3. List comprehension
string_numbers = [f"+{num}" for num in generated_numbers]
reversed_string_numbers = string_numbers[::-1]
print("List Comprehension:", string_numbers)
print("Reversed:", reversed_string_numbers)