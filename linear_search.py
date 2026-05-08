def sequentilly_search(search_element,elements):
    for i in range(len(elements)):
        if elements[i]==search_element:
            return i

input_size=int(input("Enter the input size :"))
elements=[]
print(f"Enter the {input_size} elements of the list ")
for i in range(input_size):
    element=float(input())
    elements.append(element)
return -1

print("User given elements \n",elements)
search_element=float(input("enter the element to be searched "))

search_index=sequentilly_search(search_element,elements)

if search_index==-1:
    print("element not found")
else:
    print(f"Element {search_element} found in {i}")