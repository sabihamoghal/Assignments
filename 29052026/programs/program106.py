def move_to_end(lst, element):
# Initialize a count for the specified element
  count = lst.count(element)
# Remove all occurrences of the element from the list
  lst = [x for x in lst if x != element]
# Append the element to the end of the list count times
  lst.extend([element] * count)
  return lst
