# **************  LINEAR AND BINARY SEARCH IN ORDERED ARRAYS **************** #

def linear_search(array, search_value):
    for index, element in enumerate(array):
        if element == search_value:
            print(f"Value {search_value} found at index {index}")
            return index
        elif element > search_value:
            break
    else:
        print(f"Value {search_value} does not exist within the array.")
        return None

linear_search([1, 5, 22, 33, 44, 65], 33)





def binary_search(arr, target):
    left, right = 0, len(arr) - 1 #BEGINNING INDEX AND LAST INDEX

    while left <= right: # KEEP SORTING UNTIL THE MID POINT IS REACHED
        mid = left + (right - left) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Found the target, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target is not in the array


# Example usage by calling the function directly:
result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")





