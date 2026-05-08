def binary_search(search_element,input_list):
    low=0 
    high=len(input_list)-1
    
    while low<=high :
        mid=int((low+high)/2)
        if input_list[mid] == search_element:
            return mid
        elif  input_list[mid]<search_element:
            low=mid+1
        else:
            high=mid-1