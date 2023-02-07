class Solution:
	def go(self, letter, letters, checked, letter_order):
		if checked.get(letter) is not None:
			return checked[letter]

		checked[letter] = False

		for nei in letters[letter]:
			if not self.go(nei, letters, checked, letter_order):
				return False

		checked[letter] = True
		letter_order += letter

		return True

	def alienDictionary(self, words):
		letters = {}

		for word in words:
			for ch in word:
				letters[ch] = letters.get(ch, [])

		for i in range(len(words) - 1):
			if len(words[i]) > len(words[i+1]) and words[i].startswith(words[i+1]):
				return ""

			for j in range(min(len(words[i]), len(words[i + 1]))):

				if words[i][j] != words[i + 1][j]:
					letters[words[i+1][j]].append(words[i][j])
					break

		checked = {}
		letter_order = []

		for letter in letters:
			if not self.go(letter, letters, checked, letter_order):
				return ""

		return "".join(letter_order)


if __name__ == "__main__":
    tests = [
                ["wertf", ["wrt", "wrf", "er", "ett", "rftt"]],
                ["abdce", ["acd", "aef", "bda", "dkg"]],
                ["abcde", ["abc", "aef", "bba", "bda", "chn", "dda"]],
                ["aeqr", ["ea", "qa", "qe", "rc"]],
            ]

    for test in tests:
        ans = test[0]
        try:
        	result = Solution().alienDictionary(*test[1:])
        	assert result == ans
        except AssertionError:
        	print("Error, got: %s, expected: %s" % (result, ans))
