"""
“Recently I had a visit with my mom and we realized that the two digits that make
up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
wondered how often this has happened over the years but we got sidetracked with other
topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible six times
so far. I also figured out that if we’re lucky it would happen again in a few years, and
if we’re really lucky it would happen one more time after that. In other words, it would
have happened 8 times over all. So the question is, how old am I now?”
Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string
method zfill useful.

"""

def is_reverse(a, b):
	return b == a[::-1]

def find_mom_and_my_age_difference():
	
	
	diff = 15
	while diff < 50:
		ctr = 0
		my_age = 0
		while my_age < 99:
			mom_age = my_age + diff
			if is_reverse(str(my_age).zfill(2), str(mom_age)):
				ctr += 1
				if ctr == 8:
					return diff
			my_age += 1
		
		diff += 1

def find_my_age(n):
	mom_age = n
	my_age = 0
	ctr = 0
	while my_age < 99:
		if is_reverse(str(my_age).zfill(2), str(mom_age)):
			ctr += 1
			if ctr == 6:
				return my_age
		mom_age += 1
		my_age += 1

print(find_my_age(find_mom_and_my_age_difference()))

