#!/usr/bin/env python

"""
This program accepts a url or hashtag from stdin and prints the underlying phrase without the url and hashes :

	ex: 
			'www.ieatfishes.com'	 ----> 	'i eat fishes'
			'#ILove3000' 			 ---->	'i love 3000'

"""
corpusfile = 'words.txt'
global corpus
corpus = open(corpusfile,'r').read().split()

def clean( urlhash ) :
	# returns urlhash without url decorations, hashtags, lowercase, and so just numbers and letters
	cleaned = urlhash.lower()
	
	# if hashtag
	if cleaned[0] == '#' :
		cleaned = cleaned[1:]

	# if website url
	elif cleaned[:3] == 'www' :
		firstdot = cleaned.find('.')
		seconddot = cleaned.find('.',firstdot+1)
		cleaned = cleaned[firstdot+1 : seconddot]

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

	next, remaining = urlhash, ''
	while True:
		print 'next |{}| and remaining |{}|'.format(next, remaining)
		if next in corpus or next == '' :
			break
		next, remaining = next[:-1], next[-1] + remaining 

	return (next, remaining)

if __name__ == '__main__' :

	corpusfile = 'words.txt'
	corpus = open(corpusfile,'r').read().split()

	urlhash = clean(raw_input())
	segmented_urlhash = ''

	while urlhash != '' :
		next, urlhash = get_next_token(urlhash, corpus)
		segmented_urlhash += '_'+next

	print segmented_urlhash

