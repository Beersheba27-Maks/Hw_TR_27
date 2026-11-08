import funtions_HW_6 as functions

print(f"max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100])")
print(f"-> Expected: 100 | Result: {functions.max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100])}")
print(f"max_with_negative_duplicate([10, 20, -15, -11, 20])")
print(f"-> Expected: -1 | Result: {functions.max_with_negative_duplicate([10, 20, -15, -11, 20])}\n")

print(f"sumOfTwoExists([1, -1, 40, 50, 0], 0)")
print(f"-> Expected: True | Result: {functions.sumOfTwoExists([1, -1, 40, 50, 0], 0)}")
print(f"sumOfTwoExists([1, -1, 40, 50, 0], 42)")
print(f"-> Expected: False | Result: {functions.sumOfTwoExists([1, -1, 40, 50, 0], 42)}\n")

list_to_sort = [100, 90, 80, 70]
functions.bubble_sort(list_to_sort)
print(f"bubble_sort([100, 90, 80, 70])")
print(f"-> Expected: [70, 80, 90, 100] | Result: {list_to_sort}\n")

print(f"remove_duplicates([-1, 0, 100, -1, 20, 80, 20])")
print(f"-> Expected: [-1, 0, 100, 20, 80] | Result: {functions.remove_duplicates([-1, 0, 100, -1, 20, 80, 20])}")
