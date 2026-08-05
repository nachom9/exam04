
def palindrome_partitioner(s: str) -> int:
	if s == s[::-1]:
		return 0
	pals = []
	l = len(s)
	for i in range(l - 1):
		for j in range(1, l + 1):
			sub = s[i:j]
			print(sub)
			if i != j and sub == sub[::-1]:
				pals.append((i, j))

	return(pals)



print(palindrome_partitioner("aab"))
print(palindrome_partitioner("aba"))
print(palindrome_partitioner("abc"))
