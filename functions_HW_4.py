def intersection(l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with integer numers existing in both input lists
    Examples: intersection([1, 2, 3], [4, 3, 1])=> [1, 3]
    intersection([1, 2, 3], [4, 5, 6])=> [];
    """
    result = []  
    i = 0        
    
    while i < len(l1):
        element = l1[i] 

        if element in l2:
            result.append(element)  
        i += 1 
        
    return result


def union(l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numers existing  in ether list or both
    Result list shouldn't contain repeated numbers
    Examples: union([1, 2, 3], [4, 3, 1])=> [1, 2, 3, 4]
    union([1, 2, 3], [4, 5, 6])=> [1, 2, 3, 4, 5, 6]
    """   
    result = l1.copy()  
    i = 0               
    
    while i < len(l2):
        element = l2[i] 
        
        if element not in result:
            result.append(element)  
            
        i += 1  
        
    return result  


def difference(l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numers existing  in l1
    but non-existing  l2
    Examples: difference([1, 2, 3], [4, 3, 1])=> [2]
    difference([1, 2, 3], [4, 5, 6])=> [1, 2, 3]
    """
    result = [] 
    i = 0        
    
    while i < len(l1):
        element = l1[i] 
        
        if element not in l2:
            result.append(element) 
            
        i += 1 
    return result 


def symmetric_difference(l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numers existing  in either list but not in both
    Examples: symmetric_difference([1, 2, 3], [4, 3, 1])=> [2, 4]
    symmetric_difference([1, 2, 3], [4, 5, 6])=> [1, 2, 3, 4, 5, 6]
    """  
    result = []  
    
    i = 0
    while i < len(l1):
        if l1[i] not in l2:
            result.append(l1[i])
        i += 1
   
    j = 0
    while j < len(l2):
        if l2[j] not in l1:
            result.append(l2[j])
        j += 1
        
    return result  


def remove_positive_greater_or_negative_less(numbers: list[int],
                                             positive_lim: int, negative_lim: int) -> list[int]:
    """
    numbers - list with integer numbers
    returns new list containing all numbers from the input list
    except the positive ones greater than 'positive_lim' and the negative ones
    less than 'negative_lim'
    Example: remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3)
    => [1, 2, -3, 10]
    """  
    result = []  
    i = 0        
   
    while i < len(numbers):
        x = numbers[i]  
       
        if (x > 0 and x > positive_lim) or (x < 0 and x < negative_lim):
            pass  
        else:
            result.append(x)  
            
        i += 1         
    return result 


def max_with_negative_duplicate(numbers: list[int]) -> int:
    """
    numbers - list with integer numbers
    returns the maximal element of "numbers" with existing negative duplicate 
    (example of a number with negative duplicate: number 100, negative duplicate -100)
    If no such number exists, returns -1
    Examples: max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]) => 100
    max_with_negative_duplicate([10, 20, -15, -11, 20]) => -1
    """
    max_val = -1 
    i = 0         
  
    while i < len(numbers):
        x = numbers[i] 
        
       
        if x > 0 and (-x in numbers):
            
            if max_val == -1 or x > max_val:
                max_val = x  
                
        i += 1  
        
    return max_val  
