"""
Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou? How about aeiouy?

"""
def uses_all(word, letters):
    
	for c in letters:
		if c not in word:
			return False
	return True
	
print(uses_all("Hava a nice day", "day"))
print(uses_all("Have a nice day", "days"))
