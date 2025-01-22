import copy

nested_list = [[1,2], [3,4]]
deepcopy_nested = copy.deepcopy(nested_list)
deepcopy_nested[0][1] = 99

print("Original nested list: ", nested_list)
print("Copied nested list ", deepcopy_nested)