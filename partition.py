def partition_array(numbers,low,high):
    # numbers=[]
    pivot = numbers[high]
    j = low

    for i in range(low, high):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1

    numbers[high], numbers[j] = numbers[j], numbers[high]
    return j
