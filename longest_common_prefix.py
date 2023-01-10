# The code is able to find the longest string in string array
# It had to be downgraded to only find the longest COMMON string
# Still, the code does have room for improvement.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 1:
            return strs[0]
        
        prefixes_ocurrences = {"":1}

        prefix = ""

        strs_copy = strs
        max_prefix = ""
        while strs:
            prefix = strs.pop(0)
            prefixes_ocurrences[prefix] = 1
            strs_copy = list(strs)
            for i, string in enumerate(strs_copy):
                for pref_len in range(len(prefix)):
                    #print(prefix[:len(prefix) - pref_len], "subprefix eval", prefix[pref_len:])
                    if string.startswith(prefix[:len(prefix) - pref_len]):
                        #print(prefixes_ocurrences)
                        prefixes_ocurrences[prefix[:len(prefix) - pref_len]] = prefixes_ocurrences[prefix] + 1
                        #del prefixes_ocurrences[prefix]
                        prefix = prefix[:len(prefix) - pref_len]
                        #print(strs, i, prefixes_ocurrences[prefix]-1)
                        del strs[i-(prefixes_ocurrences[prefix]-2)]
                        break
                else:
                    return ""
            break
        if prefixes_ocurrences[prefix] > prefixes_ocurrences[max_prefix]:
            max_prefix = prefix

        #print(prefixes_ocurrences,"**********")
        return max_prefix
