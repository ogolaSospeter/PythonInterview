def min_operations_for_permutable_array(arr):
    sorted_arr = sorted(arr)
    operations_counter = 0

    for i in range(len(sorted_arr)):
        operations_counter += abs(sorted_arr[i] - i)

    return operations_counter

# Example usage:
input_array = [4, 2, 1, 3,3,3,3,3,3,5,5,5,6,6,6,7,7]
result = min_operations_for_permutable_array(input_array)
print(result)
