
def scratch(x):
	for i in range(x, 0, -1):
		print(i)


# assert 12 == 13

def countdown(n):
	if n <= 0:
		return

	n -= 1
	countdown(n-1)

def countup(n):
	if n >= 0:
		countup(n-1)
		print(n)


countup(10)
