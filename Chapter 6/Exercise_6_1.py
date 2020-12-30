"""
 Write a function called is_palindrome that takes a string argument and returns True if it
is a palindrome and False otherwise. Remember that you can use the built-in function len
to check the length of a string.
"""

def is_palindrome(word):
	if word == word[::-1]:
		return True
	else:
		return False
		
print(is_palindrome("helloolleh"))

"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case.
"""
def is_power(a, b):
	if(a == b): #base case a = b
		return True
	elif(a % b != 0):
		return False
	else:
		return is_power(a/b , b)

print(is_power(8,2))
print(is_power(9,2))

"""
Write a function called gcd that takes parameters a and b and returns their greatest common divisor.
"""
def gcd(a,b):
	if (b == 0):
		return a
	else:
		return gcd(b, a%b)

		
print(gcd(105, 252))
