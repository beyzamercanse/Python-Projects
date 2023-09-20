# this is O(N) code

def has_duplicate_value(arr):
    steps = 0
    existing_numbers = {}
    
    for num in arr:
        steps += 1
        if num in existing_numbers:
            return True
        existing_numbers[num] = 1 #fix here
    
    print(steps)
    return False
result = has_duplicate_value([12,14,22,12])
print(result) # true


#
#
#
#
#


# this is O(N^2) code

def has_duplicate_value(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                return True
    return False
result = has_duplicate_value([12,14,22,12])
print(result) # true
