def average(nums: list[int]) -> float:
    """
    gives the average of the numbers in the list.
    Args:
        nums: list of integers
    Returns:
        average of the numbers in the list.
    """

    return sum(nums) / len(nums)

def median(num: list[int]) -> float:
    """
    gives the median of the numbers in the list.
    Args:
        nums: list of integers
    Returns:
        median of the numbers in the list.
    """
    return sorted(num)[len(num)//2]

def mode(num: list[int]) -> int:
    """
    gives the mode of the numbers in the list.
    Args:
        nums: list of integers
    Returns:
        mode of the numbers in the list.
    """
    return max(set(num), key=num.count)
    