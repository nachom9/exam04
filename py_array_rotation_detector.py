
def array_rotation_detector(arr1: list, arr2: list) -> bool:
	if len(arr1) != len(arr2):
		return False

	if not arr1 and not arr2:
		return True

	start_index = -1
	j = 0

	for i, a in enumerate(arr2):
		if a == arr1[0]:
			start_index = i

	if start_index == -1:
		return False

	for a in arr2[start_index:]:
		if a != arr1[j]:
			return False
		j += 1

	for a in arr2[:start_index]:
		if a != arr1[j]:
			return False
		j += 1

	return True





print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
print(array_rotation_detector([1, 2], [1, 2, 3]))
print(array_rotation_detector([], []))
print(array_rotation_detector([], [2]))
print(array_rotation_detector([3], []))
