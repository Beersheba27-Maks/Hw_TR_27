import functions_HW_9 as functions  
items_abs = [3, 5, 7, -11, 0, 4, -10, -20, 100, -80, -4, 8]
expected_abs = [0, 3, 4, 5, 7, -10, -11, -20, 100, -80, -4, 8]
functions.merge_in_place(items_abs, start=0, len1=4, size=8, key=abs)
print(f"merge_in_place abs (start=0, len1=4, size=8):\n  expected - {expected_abs}\n  actual   - {items_abs}\n")

items_mid = [99, 88, -11, 3, 7, -20, -10, 4, 77, 66]
expected_mid = [99, 88, -20, -11, -10, 3, 4, 7, 77, 66]
functions.merge_in_place(items_mid, start=2, len1=3, size=6)
print(f"merge_in_place middle default (start=2, len1=3, size=6):\n  expected - {expected_mid}\n  actual   - {items_mid}\n")

items_str = ["fig", "pear", "banana", "ki", "apple", "melon"]
expected_str = ["ki", "fig", "pear", "apple", "melon", "banana"]
functions.merge_in_place(items_str, start=0, len1=3, size=6, key=len)
print(f"merge_in_place strings by len:\n  expected - {expected_str}\n  actual   - {items_str}\n")

items_invalid = [5, 1, 2, 3]
expected_invalid = [5, 1, 2, 3]
functions.merge_in_place(items_invalid, start=-1, len1=2, size=4)
functions.merge_in_place(items_invalid, start=0, len1=2, size=10)
print(f"merge_in_place invalid bounds:\n  expected - {expected_invalid}\n  actual   - {items_invalid}\n")
