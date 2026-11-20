import functions_HW_8 as functions 

numbers: list[int] = [-3, -10, 12, 3, -21, 6, 21, 5, 4]
sorted_numbers = [-21, -10, -3, 3, 4, 5, 6, 12, 21]
sorted_numbers_abs = [-3, 3, 4, 5, 6, -10, 12, -21, 21]
sorted_even_odd = [-10, 4, 6, 12, 21, 5, 3, -3, -21]

strings: list[str] = ["banana", "apple", "kiwi", "pear", "fig"]
sorted_len_str = ["fig", "kiwi", "pear", "apple", "banana"]

part1_default = [-11, 3, 5, 7]
part2_default = [-20, -10, 0, 4]
merge_expected_default = [-20, -11, -10, 0, 3, 4, 5, 7]

part1_abs = [3, 5, 7, -11]
part2_abs = [0, 4, -10, -20]
merge_expected_abs = [0, 3, 4, 5, 7, -10, -11, -20]

print(f"bubble_sorted default:\n  expected - {sorted_numbers}\n  actual   - {functions.bubble_sorted(numbers)}\n")

print(f"bubble_sorted abs:\n  expected - {sorted_numbers_abs}\n  actual   - {functions.bubble_sorted(numbers, abs)}\n")

print(f"even_asc_odd_desc:\n  expected - {sorted_even_odd}\n  actual   - {functions.even_asc_odd_desc(numbers)}\n")

print(f"bubble_sorted strings (len, str):\n  expected - {sorted_len_str}\n  actual   - {functions.bubble_sorted(strings, lambda s: (len(str(s)), s))}\n")

print(f"merge default:\n  expected - {merge_expected_default}\n  actual   - {functions.merge(part1_default, part2_default)}\n")

print(f"merge abs:\n  expected - {merge_expected_abs}\n  actual   - {functions.merge(part1_abs, part2_abs, abs)}\n")
