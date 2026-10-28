# 1
def indexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its first occurrence,
        otherwise -1.
    """
    for index, value in enumerate(numbers):
        if value == num:
            return index
    return -1

test_list1 = [10, 20, 30, 20, -1]

print("Index of first 20:", indexOf(test_list1, 20))  
print("Index of 23:", indexOf(test_list1, 23)) 

# 2
def lastIndexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its last occurrence,
        otherwise -1.
    """
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] == num:
            return i
    return -1

test_list2 = [10, 20, 30, 20, -1]

print("Index of last 20:", lastIndexOf(test_list2, 20))  
print("Index of last -1:", lastIndexOf(test_list2, -1)) 
print("Index of 100:", lastIndexOf(test_list2, 100))

# 3
def min_even(numbers):
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked ) 
    """ 
    min_val = None
    for num in numbers:
        if num % 2 == 0:
            if min_val is None or num < min_val:
                min_val = num
    return min_val

test_list3 = [-1, 10, 20, 8, -7, -2]

print("Minimal even number:", min_even(test_list3))

# 4
def count(numbers, num):
    """
    "numbers" - list with int numbers; "num" - int
    returns count of "num" occurrences in "numbers".
    """
    counter = 0
    for value in numbers:
        if value == num:
            counter += 1
    return counter

test_list4 = [10, 20, 30, 20, -1, 20]

print("Count of 20:", count(test_list4, 20)) 
print("Count of 50:", count(test_list4, 50))     

# 5
def sumOfTwoExists(numbers, sum_val):
    """
    Optional task for advanced students
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    """ 
    seen = set()
    for current_num in numbers:
        if (sum_val - current_num) in seen:
            return True
        seen.add(current_num)
    return False

advanced_list = [1, -1, 40, 50, 0]

print("Sum 0 exists:", sumOfTwoExists(advanced_list, 0))    
print("Sum 42 exists:", sumOfTwoExists(advanced_list, 42))  