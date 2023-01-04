class Solution(object):
	def isAlienSorted(words, order):
	    """
	    :type words: List[str]
	    :type order: str
	    :rtype: bool
	    """
	    prev_word = ""

	    for word in words:
	        for letter_i in range(len(prev_word)):
	            prev_let_ord = order.index(prev_word[letter_i])
	            if len(word) - 1 < letter_i:
	                if len(prev_word) > len(word):
	                	return False
	                else:
	                	break
	            let_ord = order.index(word[letter_i])
	            if prev_let_ord > let_ord:
	                return False
	            elif prev_let_ord < let_ord:
	                break
	        prev_word = word

	    return True
