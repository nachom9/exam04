
def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
	row_count = 0
	result = []

	for i in range(size):
		row = ''
		for j in range(size):
			row += '.'
		result.append(row)

	for a in stars:
		result[a[0]][a[1]] = '*'

	return result









print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
