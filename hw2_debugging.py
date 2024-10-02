""" Module providing random functionality"""
import rand


def merge_sort(arr):
    """
    Merge sort functionality
    IN: arr - an array of values
    OUT: merged_arr - an updated, merged array
    """
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    # """
    # A helper function to combine two arrays
    # IN: left_arr - the left array to combine
    # IN: right_arr - the right array to combine
    # OUT: merge_arr - the merged array
    # """
    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])

    return merge_arr


array = rand.random_array([None] * 20)
arr_out = merge_sort(array)

print(arr_out)
