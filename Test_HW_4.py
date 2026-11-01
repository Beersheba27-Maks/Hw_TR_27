import functions_HW_4 as functions

print(f"intersection([1, 2, 3], [4, 3, 1]) -> Expected: [1, 3] | Result: {functions.intersection([1, 2, 3], [4, 3, 1])}")
print(f"intersection([1, 2, 3], [4, 5, 6]) -> Expected: [] | Result: {functions.intersection([1, 2, 3], [4, 5, 6])}\n")

print(f"union([1, 2, 3], [4, 3, 1]) -> Expected: [1, 2, 3, 4] | Result: {functions.union([1, 2, 3], [4, 3, 1])}")
print(f"union([1, 2, 3], [4, 5, 6]) -> Expected: [1, 2, 3, 4, 5, 6] | Result: {functions.union([1, 2, 3], [4, 5, 6])}\n")

print(f"difference([1, 2, 3], [4, 3, 1]) -> Expected: [2] | Result: {functions.difference([1, 2, 3], [4, 3, 1])}")
print(f"difference([1, 2, 3], [4, 5, 6]) -> Expected: [1, 2, 3] | Result: {functions.difference([1, 2, 3], [4, 5, 6])}\n")

print(f"symmetric_difference([1, 2, 3], [4, 3, 1]) -> Expected: [2, 4] | Result: {functions.symmetric_difference([1, 2, 3], [4, 3, 1])}")
print(f"symmetric_difference([1, 2, 3], [4, 5, 6]) -> Expected: [1, 2, 3, 4, 5, 6] | Result: {functions.symmetric_difference([1, 2, 3], [4, 5, 6])}\n")

print(f"remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3)")
print(f"-> Expected: [1, 2, -3, 10] | Result: {functions.remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3)}\n")

print(f"max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]) -> Expected: 100 | Result: {functions.max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100])}")
print(f"max_with_negative_duplicate([10, 20, -15, -11, 20]) -> Expected: -1 | Result: {functions.max_with_negative_duplicate([10, 20, -15, -11, 20])}")
