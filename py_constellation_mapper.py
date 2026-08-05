
def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
	row_count = 0
	star_list = []
	result = []

	if size < 1:
		return []

	for i in range(size):
		for j in range(size):
			star_list.append('.')

	for star in stars:
		coords = (star[0] * size) + star[1]
		if coords <= len(star_list):
			star_list[coords] = '*'

	for i in range(size):
		row = ''
		for j in range(size):
			row += star_list[i * size + j]
		result.append(row)
	return result


print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
print(constellation_mapper([(0, 0), (0, 1), (0, 2), (1, 1), (2, 2)], 3))
print(constellation_mapper([(0, 0), (5, 5), (2, 2)], 3))
print(constellation_mapper([(0, 0), (5, 5), (5, 5), (2, 2)], 3))
print(constellation_mapper([(0, 0), (5, 5)], 2))
print(constellation_mapper([(0, 0), (5, 5)], 0))
