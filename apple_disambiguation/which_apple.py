#!/usr/bin/env python

"""
(Basic explanation)
"""

def whichApple(text) :
	"""
	Predicts whether text refers to apple - the fruit or Apple - the company.
	Right now only based on last appearance of word "apple" in the text

	Requires: 'apple' to appear in text (with or without capitals)
	Returns: 'fruit' or 'computer-company'
	"""

	
	return 'computer-company' #or fruit

if __name__ == '__main__' :

	#formatted to accept Hackerrank like input
	iterations = int(raw_input())
	for num in xrange(iterations) :

		text = raw_input()
		print whichApple(text)


