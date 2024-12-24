def print_butterfly(n):
	for i in range(n):
		print("*" * (i+1) + " " * (n - i - 1) + " " * (n - i - 1) + "*" * (i+1))

	for i in range(n - 2, -1, -1):
		print("*" * (i+1) + " " * (n - i - 1) + " " * (n - i - 1) + "*" * (i+1))

print_butterfly(10)
input()
