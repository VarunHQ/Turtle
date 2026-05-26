lst = ["Orange", "Kiwi", "Grapes", "Mango", "Pineapple"]

print("Length of the list is:", len(lst))
print("First element of the list is:", lst[0])
print("Last element of the list is:", lst[-1])

lst.append("Kiwi")
print("List after appending 'Kiwi':", lst)

lst.remove("Grapes")
print("List after removing 'Grapes':", lst)

lst.sort()
print("List after sorting:", lst)

lst.pop(3)
print("List after popping the element at index 3:", lst)

lst.reverse()
print("List after reversing:", lst)

print("Multiplication of list:", lst*2)

lst = lst[:4]
print("List after slicing to first 4 elements:", lst)

lst.clear()
print("List after clearing:", lst)