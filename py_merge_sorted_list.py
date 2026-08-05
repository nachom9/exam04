
def merge_sorted_list(lists: list[list[int]]) -> list[int]:
	return sorted([n for l in lists for n in l])


print(merge_sorted_list([[1, 4, 5], [1, 3, 4], [2, 6]]))
print(merge_sorted_list([[1, 2, 3], [], [0, 4]]))
print(merge_sorted_list([]))
print(merge_sorted_list([[], []]))
