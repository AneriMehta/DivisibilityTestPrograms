def isDivBy16(n):
	last_four_digits = int(n[-4:])
	result = last_four_digits / 16
	if result.is_integer():
		return True
	else:
		return False


for i in range(10000):
	print(f'{i} is divisible by 16? {isDivBy16(str(i))}')