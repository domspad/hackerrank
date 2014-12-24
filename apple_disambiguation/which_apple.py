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
	instance, location = extractApple(text)

	#coding the decision tree model
	if instance[0].isupper() :
		if sentenceStart(text, index) :
			if isPlural(instance) :
				return 'fruit'
			else :
				return 'computer-company'
		else :
			return 'computer-company'
	else :
		return 'fruit'

def extractApple(text) :
	"""
	Requires: some form of 'apple' shows up in text (i.e. capitalized, plural, possessive)
	Returns: the form of the first instance found and its starting index in the text
	"""
	# words = text.split()

	# prev = ''
	# for index,word in enumerate(words) :
	# 	#is word a variant of apple<'><s><'>?
	# 	if word[:5].lower() == 'apple' and len(word.lower().replace("'","")) <= 6 : #like applet...
	# 		#capital?
	# 		if word[0].isupper() :
	# 			+1 for company!
	# 		#plural?

	# 		#after end of sentence?
	return 'Apple',0

def whichApple_tests() :
	testcase_file = './test_cases.txt'
	with open(testcase_file, 'r') as f :
		num = int(f.readline())
		for i in xrange(num) :
			answer, text = f.readline().split('||')
			assert whichApple(text) == answer
	return

if __name__ == '__main__' :

	whichApple_tests()

	#formatted to accept Hackerrank like input
	iterations = int(raw_input())
	for num in xrange(iterations) :

		text = raw_input()
		print whichApple(text)


