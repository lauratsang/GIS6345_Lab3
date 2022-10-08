
'''
1. Type these functions into a file named palindrome.py and test them out.
If you call middle with anything less than three letters, nothing is returned, it just
prints out a blank line.

2. Write a function called is_palindrome.
'''
>>> from __future__ import print_function, division
>>> def first(word):
	return word[0]

>>> def last(word):
	return word[-1]

>>> def middle(word):
	return word[1:-1]

>>> def is_palindrome(word):
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False
	return is_palindrome(middle(word))
