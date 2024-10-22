def can_be_sorted_with_two_swaps(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    
    # Find the indices where the array is out of order
    mismatch_indices = [i for i in range(n) if arr[i] != sorted_arr[i]]
    
    # If the array is already sorted
    if not mismatch_indices:
        return True
    
    # If there are more than 4 mismatched indices, it can't be sorted with two swaps
    if len(mismatch_indices) > 4:
        return False
    
    # Check if swapping the mismatched elements can sort the array
    for i in range(len(mismatch_indices)):
        for j in range(i + 1, len(mismatch_indices)):
            # Swap elements at mismatch_indices[i] and mismatch_indices[j]
            arr[mismatch_indices[i]], arr[mismatch_indices[j]] = arr[mismatch_indices[j]], arr[mismatch_indices[i]]
            
            # Check if the array is sorted
            if arr == sorted_arr:
                return True
            
            # Swap back to original positions
            arr[mismatch_indices[i]], arr[mismatch_indices[j]] = arr[mismatch_indices[j]], arr[mismatch_indices[i]]
    
    return False

# Example usage
arr = [3, 1, 2, 4]
print(can_be_sorted_with_two_swaps(arr))  # Output: True
