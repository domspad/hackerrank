#!/usr/bin/env python

"""
This program accepts a url or hashtag from stdin and prints the underlying phrase without the url and hashes :

	ex: 
			'www.ieatfishes.com'	 ----> 	'i eat fishes'
			'#ILove3000' 			 ---->	'i love 3000'

"""

def clean( urlhash ) :
	# returns urlhash without url decorations, hashtags, lowercase, and so just numbers and letters
	cleaned = urlhash.lower()
	
	# if hashtag
	if cleaned[0] == '#' :
		cleaned = cleaned[1:]

	# if website url

	"""
	contains '.'
		start 
			if http<s>://
			if www.
			
			(-
			www.
			http<s>://
			http<s>://www.)

		end
			remove after next dot

			(.com
			.co.uk
			.sfgov.org/
			.io/)
	"""
	#check if webaddress
	elif '.' in cleaned :
		#remove possible prefixes
		if cleaned[:8] == 'https://' :
			cleaned = cleaned[8:]
		elif cleaned[:7] == 'http://' :
			cleaned = cleaned[7:]
		if cleaned[:4] == 'www.' :
			cleaned = cleaned[4:]

	#remove suffixes by removing everything after next dot
		nextdot = cleaned.find('.')
		cleaned = cleaned[:nextdot]

	# outside cases we consider
	else :
		'neither?!'
	# for any lingering non-alphanumeric characters
	validchars = 'abcdefghijklmnopqrstuvwxyz0123456789'
	cleaned = ''.join(char for char in cleaned if char in validchars)

	return cleaned

def get_next_token( urlhash , corpus ) :
	#returns the longest possible token starting from the left
	#if no token returns ''
	cand, remaining = urlhash, ''

	#handle the number case...
	if urlhash[0].isdigit() :
		for ind, char in enumerate(cand) :
			if not char.isdigit() :
				cand, remaining = cand[:ind], cand[ind:]
				break
		return cand, remaining

	while True:
		# print 'cand |{}| and remaining |{}|'.format(cand, remaining)
		if cand in corpus or cand == '' :
			break
		cand, remaining = cand[:-1], cand[-1] + remaining 

	return (cand, remaining)

def segment( urlhash ) :
	#The main function
	#returns the segmented version of the given url or hashtag (without the url and hashtage features)
	tokens = []

	while urlhash != '' :
		cand, urlhash = get_next_token(urlhash, corpus)
		tokens.append(cand)

	return ' '.join(tokens)

if __name__ == '__main__' :

	corpusfile = 'words.txt'
	corpus = open(corpusfile,'r').read().lower().split()

	iterations = int(raw_input())
	for num in xrange(iterations) :

		urlhash = clean(raw_input())
		print segment(urlhash)

