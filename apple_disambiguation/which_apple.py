#!/usr/bin/env python

"""
(Basic explanation)
"""

def whichApple(text) :
	return 'computer-company\n' #or fruit

if __name__ == '__main__' :

	#formatted to accept Hackerrank like input
	iterations = int(raw_input())
	for num in xrange(iterations) :

		text = raw_input()
		print whichApple(text)


