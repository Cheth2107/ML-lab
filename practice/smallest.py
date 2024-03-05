Python Program to find smallest number in a tuple

def find_smallest_item(input_tuple):
    if not input_tuple:
        return None  # Return None if tuple is empty
    smallest_item = input_tuple[0]  # Assume the first item is the smallest
    for item in input_tuple:
        if item < smallest_item:
            smallest_item = item
    return smallest_item

# Example usage:
input_tuple = (5, 3, 8, 2, 10, 1)
smallest_item = find_smallest_item(input_tuple)
print("The smallest item in the tuple is:", smallest_item)
