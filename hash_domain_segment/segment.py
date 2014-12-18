#!/usr/bin/env python

"""
This program accepts a url or hashtag from stdin and prints the underlying phrase without the url and hashes :

	ex: 
			'www.ieatfishes.com'	 ----> 	'i eat fishes'
			'#ILove3000' 			 ---->	'i love 3000'

"""

def clean( urlhash ) :
	# returns urlhash without url decorations, hashtags, lowercase, and so just numbers and letters
	return cleaned

def get_next_token( urlhash ) :
	#returns the longest possible token starting from the left
	return (next, remaining)

if __name__ == '__main__' :
	urlhash = raw_input()
	segmented_urlhash = ''

	while urlhash != '' :
		next, urlhash = get_next_token(urlhash)
		segmented_urlhash += next

	print segmented_urlhash

