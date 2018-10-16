c = int(input())
for _ in range(c):
	x, y, n = [int(s) for s in input().split()]
	for i in range(1, n+1):
		if i % x == 0 and i % y == 0:
			print("FizzBuzz")
		elif i % x == 0:
			print("Fizz")
		elif i % y == 0:
			print("Buzz")
		else:
			print(i)