import math

# math
def count_digits(num):
	digits = 0
	while num > 0:
		num //= 10
		digits += 1
	
	return digits

# logarithms
def count_digits_log(num):
	return math.floor(math.log10(num) + 1)


# strings
def count_digits_string(num):
    return len(str(num))
