# 1
def indexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its first occurrence,
        otherwise -1.
    """
    if num in numbers:
        return numbers.index(num)
    return -1

test_list = [10, 20, 30, 20, -1]

result1 = indexOf(test_list, 20)
print("Result for 20:", result1)

result2 = indexOf(test_list, 23)
print("Result for 23:", result2) 

# 2
def lastIndexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its last occurrence,
        otherwise -1.
    """
    if num not in numbers:
        return -1
    
    reversed_numbers = numbers[::-1]
    
    index_from_end = reversed_numbers.index(num)
    original_index = len(numbers) - 1 - index_from_end
    
    return original_index

test_list = [10, 20, 30, 20, -1]

result1 = lastIndexOf(test_list, 20)
print("Result for 20:", result1)

result2 = lastIndexOf(test_list, -1)
print("Result for -1:", result2)

# 3
def min_even(numbers):
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked ) 
    """ 
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    return min(even_numbers)

test_list = [-10001, 10, 20, 8, -7]

result = min_even(test_list)
print("Minimal even number:", result)

# 4
def count(numbers, num):
    """
    "numbers" - list with int numbers; "num" - int
    returns count of "num" occurrences in "numbers".
    """
    return numbers.count(num)

test_list = [10, 20, 30, 20, -1]

result1 = count(test_list, 20)
print("Count of occurrences of 20:", result1)

result2 = count(test_list, 23)
print("Count of occurrences of 23:", result2)

# 5
def sumOfTwoExists(numbers, sum_val):
    """
    Optional task for advanced students
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    """ 
    for i in range(len(numbers)):
        current_num = numbers[i]
        needed_num = sum_val - current_num
        remaining_numbers = numbers[i + 1:]

        if needed_num in remaining_numbers:
            return True
            
    return False

advanced_list = [1, -1, 40, 50, 0]

result1 = sumOfTwoExists(advanced_list, 0)
print("Result for sum 0:", result1) 

result2 = sumOfTwoExists(advanced_list, 42)
print("Result for sum 42:", result2)  