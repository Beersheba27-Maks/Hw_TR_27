def binary_search(numbers: list[int], num: int) -> int:
    """
    O[logN]
    numbers: sorted list
    num: being searched number
    returns an inedex of the first occurrence at which "num" resides in "numbers" or 
    negative number as -(index_sort + 1) where index_sort is the index where "num" should have been in "numbers"
    for example: numbers: list[int] =
    binary_search(numbers, 20) -> 3 (not 4),binary_search(numbers, 15) -> -4 (not -1),
    binary_search(numbers, 45) -> -10
    """
    left: int = 0
    right: int = len(numbers) - 1
    result: int = -1

    while left <= right:
        mid: int = (left + right) // 2
        if numbers[mid] == num:
            result = mid
            right = mid - 1
        elif numbers[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return result if result != -1 else -(left + 1)


def insert_sorted(numbers: list[int], num: int) -> None:
    """
    numbers: sorted list
    num: inserted number
    inserts "num" keeping "numbers" sorted
    For example: numbers: list[int] =
    after insert_sorted (numbers, 19) the list will contain
    after insert_sorted (numbers, 20) (initial list) the list will contain

    """
    index: int = binary_search(numbers, num)
    if index < 0:
        index = -(index + 1)
    numbers.insert(index, num)
