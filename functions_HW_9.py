from typing import Callable


def __move_min2_to_place[T, K](items: list[T], /, *, start: int, stop: int,
                               key: Callable[[T], T | K]) -> None:
    while start < stop and key(items[start]) > key(items[start + 1]):  # type: ignore
        items[start], items[start + 1] = items[start + 1], items[start]
        start += 1


def merge_in_place[T, K](items: list[T], start: int, len1: int, size: int,
                         key: Callable[[T], K | T] | None = None) -> None:
    """
    merges two sorted by key subparts in place of a list's part
    Time complexity O[N^2]
    Space complexity O[1] no additional list is created
    items - list of T objects (T any type generic at call time)
    start - start index of a being merged list
    len1 - length of the first subpart
    size - length of whole part
    Example: items - [3, 5, 7, -11, 0, 4, -10, -20, 100, -80,-4, 8 ], key - abs function
    start - 0; len1 - 4; size - 8
    call as  merge_in_place(items, start=0, len1=4, size=8, key=abs)
    updated items should be as [0, 3, 4, 5, 7, -10, -11, -20, 100, -80,-4, 8]
    """
    if 0 < len1 < size and start >= 0 and start + size <= len(items):
        i_min_2 = start + len1
        stop = start + size - 1
        i = start
        i_max_1 = start + len1 - 1
        if key is None:
            key = lambda a: a
        while (key_min2 := key(items[i_min_2])) < key(items[i_max_1]):  # type: ignore
            if key(items[i]) > key_min2:  # type: ignore
                items[i], items[i_min_2] = items[i_min_2], items[i]
                __move_min2_to_place(items, start=i_min_2, stop=stop, key=key)
            i += 1
