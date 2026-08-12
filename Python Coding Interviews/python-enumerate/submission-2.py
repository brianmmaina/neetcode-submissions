from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i, digit in enumerate(nums):
        if digit == 7:
            return i
        
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    start = -1
    end = -1
    for i, digit in enumerate(nums):
        
        
        if start == -1 and digit == 7:
            start = i

        elif start != -1 and end == -1 and digit == 7:
            end = i
      
    return end - start


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
