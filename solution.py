def solution(array, subset_length):
    # check if the length of the array is less than the length of the subset
    if len(array) < subset_length:
        return "Error: length of the array is less than the length of the subset"
    
    # list to store the minimum values of each subset
    min_values = []

    # Loop to create subsets and find the minimum value
    for i in range(len(array) - subset_length + 1):
        subset = array[i:i + subset_length]
        # print(subset)
        min_values.append(min(subset))
    
    # get the maximum value from the list of minimum values
    max_min_value = max(min_values)
    
    return max_min_value

if __name__ == "__main__":
    # input array
    array_input = input("input the array (comma separated): ")
    array = [int(x) for x in array_input.split(',')]
    
    # input subset length
    subset_length = int(input("input the length of subset: "))
    
    # call the function and print the result
    result = solution(array, subset_length)
    print("Result:", result)
