
def palindrome_partitioner(s: str) -> int:
	result = []
	result_b = []
	pals = []
	l = len(s)
	for i in range(0, l):
		for j in range(i, l):
			sub = s[i:j + 1]
			if sub == sub[::-1]:
				pals.append((i, j))

	i = 0
	while i < l:
		smallest, largest = i, max(n for pal in pals for n in pal if pal[0] == i)
		result.append((smallest, largest))
		i = max(i + 1, largest - smallest + 1)

	i = l - 1
	while i >= 0:
		smallest, largest = min(n for pal in pals for n in pal if pal[1] == i), i
		result_b.append((smallest, largest))
		i = min(i - 1, smallest - 1)
	return min(len(result), len(result_b)) - 1



tests = [
    # Casos base
    ("a", 0),
    ("ab", 1),
    ("abc", 2),
    ("abcd", 3),

    # Todo palíndromo
    ("aa", 0),
    ("aba", 0),
    ("abba", 0),
    ("abcba", 0),
    ("abccba", 0),
    ("racecar", 0),
    ("aaaaaa", 0),

    # Un único corte
    ("aab", 1),             # aa | b
    ("abb", 1),             # a | bb
    ("baa", 1),             # b | aa
    ("banana", 1),          # b | anana
    ("abbacdc", 1),         # abba | cdc
    ("abcddcbae", 1),       # abcddcba | e
    ("abcdedcbaxyzyx", 1),  # abcdedcba | xyzyx
    ("aabb", 1),            # aa | bb

    # Dos cortes
    ("noonabbad", 2),       # noon | abba | d
    ("cddpd", 2),           # c | d | dpd
    ("aabc", 2),            # aa | b | c
    ("abcc", 2),            # a | b | cc
    ("abbacd", 2),          # abba | c | d

    # Casos clásicos difíciles
    ("ababbbabbababa", 3),
    ("cabababcbc", 3),

    # Sin apenas palíndromos
    ("abcdef", 5),
    ("abcdefgh", 7),

    # Mucha repetición
    ("aaaaaaaaab", 1),
    ("baaaaaaaaa", 1),
]

for s, esperado in tests:
    obtenido = palindrome_partitioner(s)
    print(
        f"{'OK ' if obtenido == esperado else 'ERR'} "
        f"{esperado:2} | {obtenido:2} | {s}"
    )
