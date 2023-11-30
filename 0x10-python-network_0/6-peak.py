#!/usr/bin/python3

""" Find a peak """


def find_peak(nums):
    """
    Finds a peak in the given list of numbers using binary search.
    """
    n = len(nums)

    if n == 0:
        return

    left, right = 0, n - 1

    while left < right:
        mid = left + (right - left) // 2

        # Compare the mid element with its neighbor
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    # 'left' will point to a peak element
    return nums[left]
