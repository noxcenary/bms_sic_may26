def divide_array(numbers,low,high):

    if low<high:
        mid=(low+high)//2
        divide_array(numbers,low,mid)
        divide_array(numbers,mid+1,high)
        merged = merge(numbers[low:mid+1],numbers[mid+1:high+1])
        for i in range(len(merged)):
            numbers[low+i] = merged[i]



def merge(array_a,array_b):
    merged_array=[]
    i=j=0
    while(i<len(array_a) and j<len(array_b)):
        if array_a[i]<array_b[j]:
            merged_array.append(array_a[i])
            i+=1
        else:
            merged_array.append(array_b[j])
            j+=1
        
    merged_array.extend(array_b[j:])
    merged_array.extend(array_a[i:])
    return merged_array
