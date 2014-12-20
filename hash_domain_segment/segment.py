#!/usr/bin/env python

"""
This program accepts a url or hashtag from stdin and prints the underlying phrase without the url and hashes :

	ex: 
			'www.ieatfishes.com'	 ----> 	'i eat fishes'
			'#ILove3000' 			 ---->	'i love 3000'

Assumed possible url forms:

			prefixes : combinations of 'http<s>://' and 'www.' and ''
			suffixes : anything after first '.' AFTER the prefixes have been removed

Assumed hashtag form : #<alpha,nums>

"""

def dropUrlPrefix(url) :
	"""
	Requires : 
	Returns : returns url without prefix '<http<s>://><www.>'  
	"""
	if len(url) >= 8 and url[:8] == 'https://' :
		url = url[8:]
	elif len(url) >= 7 and url[:7] == 'http://' :
		url = url[7:]
	if len(url) >= 4 and url[:4] == 'www.' :
		url = url[4:]
	return url

def dropUrlSuffix(url) :
	"""
	Requires : '.' in url 
	Returns : url without any suffixes like '.com', '.co.uk',...
	"""
	nextdot = url.find('.')
	url = url[:nextdot]
	return url


def clean( urlhash ) :
	"""
	Requires : urlhash at least one characters
	Returns : urlhash without hashtag or url decorations (just concatenated lowercase letters and numbers)
	"""
	cleaned = urlhash.lower()
	
	# if hashtag
	if cleaned[0] == '#' :
		cleaned = cleaned[1:]

	#check if url
	elif '.' in cleaned :
		cleaned = dropUrlPrefix(cleaned)
		cleaned = dropUrlSuffix(cleaned)
	
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

