"""Subprocess module"""
import subprocess

def random_array(arr):
    """
    Creates an array of random values
    IN: arr - an array
    OUT: arr - the randomized array
    """
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
