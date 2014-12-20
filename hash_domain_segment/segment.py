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


def isDone( remaining ) :
	"""
	Returns : True if remaining is empty string, else False
	"""
	return remaining == ''


def goDown( remaining, limit, corpus ) :
	"""
	Steps down the search tree

	Requires: limit <=len(remaining)+1, remaining != ''
	Returns : longest valid substring (of length < limit) from remaining starting from beginning (in corpus or is number)
				otherwise, returns '' 
	"""
	longest  = remaining[:limit-1]

	#handle the number case...
	if longest[0].isdigit() :
		for ind, char in enumerate(longest) :
			if not char.isdigit():
				longest = longest[:ind]	
				break			
		return longest


	#handle the word case
	while True:
		if longest in corpus or longest == '' :
			break
		longest = longest[:-1]

	return longest


def putBack( tokens, remaining ):
	"""
	Moves back up the tree and sets up so next search step goes down next branch (if there)

	Requires : tokens non empty
	Effects : pops element from tokens if nonempty
	Returns : tokens with one less token, and remaining prefixed with popped token, and size of popped token
				if tokens == []  then limit == 0
	"""
	try :
		last_token = tokens.pop()
		remaining = last_token + remaining
		limit = len(last_token)

	except IndexError :
		limit = 0

	return remaining, limit

def tokenize(urlhash, corpus) :
	"""
	The main algorithm -- performs depth first search to tokenize the urlhash into words

	Returns : tokenized version of urlhash (as string) 
				if not possible to tokenize given corpus, then returns 'FAILURE {}'.format(urlhash)
	"""
	tokens = []
	remaining = urlhash
	limit = len(urlhash) + 1

	while not isDone(remaining) :
		next_token = goDown(remaining, limit, corpus)
		
		#cant descend tree, must move to next branch
		if next_token == '' :
			remaining, limit = putBack(tokens, remaining)
			
			# tokens was empty so there are no ways to tokenize the urlhash!
			if limit == 0 :
				return 'FAILURE TO TOKENIZE {}'.format(urlhash)

			continue

		#successful goDown so update state
		tokens.append(next_token)
		remaining = remaining[len(next_token):]
		limit = len(remaining)+1

	tokenized = ' '.join(tokens)

	return tokenized


if __name__ == '__main__' :

	corpusfile = 'words.txt'
	corpus = open(corpusfile,'r').read().lower().split()

	iterations = int(raw_input())
	for num in xrange(iterations) :

		urlhash = clean(raw_input())
		print tokenize(urlhash)

