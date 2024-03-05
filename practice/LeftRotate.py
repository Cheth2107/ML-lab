//Python Program to Left Rotate a NumPy array by n

import numpy as np

def left_rotate_array(arr, n):
    """
    Left rotate a NumPy array by n elements.
    
    Parameters:
    - arr: NumPy array to be rotated
    - n: Number of elements to rotate by
    
    Returns:
    - Rotated NumPy array
    """
    length = len(arr)
    n = n % length  # Ensure that n is within the length of the array
    
    if n == 0:
        return arr
    else:
        return np.concatenate((arr[n:], arr[:n]))

# Example usage:
if __name__ == "__main__":
    arr = np.array([1, 2, 3, 4, 5])
    n = 2
    rotated_arr = left_rotate_array(arr, n)
    print("Original array:", arr)
    print("Left rotated array by", n, "elements:", rotated_arr)
