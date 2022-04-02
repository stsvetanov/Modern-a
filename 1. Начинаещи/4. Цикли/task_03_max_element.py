# find the biggest elements of the list and print the result

elements = [3, 5, 34, 2, 3, 43, 34.3, -23, 23]

# Ver 1
max_element = elements[0]

for element in elements:
    if element > max_element:
        max_element = element

print(max_element)

# Ver 2
# print(max(elements))
