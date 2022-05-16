def enum(alpha, n):
	if n == 0:
		return [""]
	current = []
	next = enum(alpha, n-1)
	for i in alpha:
		for j in next:
			if not (i == '' and j != ''):
				current.append(i + j)
	return current

alpha = ['S' ,'J' ,'K' ,'X' ,'W' ,'V' ,'D' ,'O' ,'N' ,'R', 'I' ]

n = 3

for i in enum(alpha, n):
	print(i)