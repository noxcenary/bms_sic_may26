import sys
import binary_search

input_numbers=[]

for i in  range(1,len(sys.argv)):
    input_numbers.append(float(sys.argv[i]))

print(f"User given elements are \n",input_numbers)

search_element=float(input("enter the element to be searched "))

search_index=binary_search.binary_search(search_element,input_numbers)

if search_index==-1:
    print("element not found")
else:
    print(f"Element {search_element} found in index {search_index}")





