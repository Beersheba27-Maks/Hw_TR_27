from typing import Callable, Sequence

def __move_max_to_end[T](objects: list[T], size: int,
                         key: Callable[[T], object]) -> int:
    n_swaps = 0
    for i in range(size):
        if key(objects[i]) > key(objects[i + 1]): 
            n_swaps += 1
            objects[i], objects[i + 1] = objects[i + 1], objects[i]
    return n_swaps

def bubble_sorted[T](items: Sequence[T],
                     key: Callable[[T], object] | None = None) -> list[T]:
    """
    Sequence[T] means immutable sequence, so items cannot be updated.
    Returns new list of objects sorted using algorithm "bubble sort"
    in accordance with key function-converter like standard Python sorting.
    items - sequence of any objects
    key - a function taking one object and returning converted object having standard operator ">"
    default value None designating standard Python sorting with no converting initial object
    For example, bubble_sorted(numbers) - regular sort of numbers
    bubble_sorted(numbers, abs) - sort of numbers in accordance with their abs values
    Unlike the standard sorting methods of Python, the function may be called with no explicit specifying key=
    """
    result = list(items)
    if key is None:
        key = lambda obj: obj

    unsorted = True
    size = len(items)

    while unsorted:
        size -= 1
        unsorted = bool(__move_max_to_end(result, size, key))
    return result


def even_asc_odd_desc(numbers: list[int]) -> list[int]:
    """
    Returns new list of numbers sorted in the following order:
    The even numbers ordered by ascending order reside before odd numbers ordered by descending order.
    For example, even_asc_odd_desc([-3, -10, 12, 3, -21, 6, 21, 5, 4 ]) returns [-10, 4, 6, 12, 21, 5, 3, -3, -21]
    """
    return sorted(numbers, key=lambda num: (1, -num) if num % 2 else (0, num))


def merge[T](part1: Sequence[T], part2: Sequence[T],
             key: Callable[[T], object] | None = None) -> list[T]:
    """
    part1 and part2 - sorted in accordance with key function-converter sequences of any objects
    key - a function taking one object and returning converted object having standard operator ">"
    default value None designating standard Python sorting with no converting initial object
    Returns new list, sorted in accordance with key function-converter, comprising of two sequences-parts.
    For example, merge([-11, 3, 5, 7], [-20, -10, 0, 4]) => [-20, -11, -10, 0, 3, 4, 5, 7]
    merge([3, 5, 7, -11], [0, 4, -10, -20], abs) => [0, 3, 4, 5, 7, -10, -11, -20]
    """
    result: list[T] = []
    i1 = i2 = 0
    len1, len2 = len(part1), len(part2)

    if key is None:
        key = lambda obj: obj
    while i1 < len1 and i2 < len2:
        if key(part1[i1]) > key(part2[i2]):
            result.append(part2[i2])
            i2 += 1
        else:
            result.append(part1[i1])
            i1 += 1
    result.extend(part1[i1:])
    result.extend(part2[i2:])

    return result
