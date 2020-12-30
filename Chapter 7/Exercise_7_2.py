"""
The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of 1/π:
Write a function called estimate_pi that uses this formula to compute and return an estimate of
π. It should use a while loop to compute terms of the summation until the last term is smaller than
1e-15 (which is Python notation for 10−15). You can check the result by comparing it to math.pi.
"""



import math


def estimate_pi():
	sum = 0
	epsilon = math.pow(10, -15)
	k = 0
	i = 1 #initialize i, the value doesn't matter
	while i > epsilon:
		i = (math.factorial(4*k) * (1103 + 26390 * k)) / (math.pow((math.factorial(k)), 4) * math.pow(396, 4*k) )
		sum += i
		k += 1 #!important
	inverse = 2 * math.sqrt(2) * sum / 9801
	return 1/inverse
	
print(estimate_pi())
print(math.pi)
print(estimate_pi() - math.pi)
