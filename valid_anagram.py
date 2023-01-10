# Considering we are doing two loops sorting would be a better option

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        already_check = []
        for let in s:
            if let in already_check:
                continue
            rep_count = 0
            for let_check in s:
                if let_check == let:
                    rep_count += 1
            already_check.append(let)
            rep_t_count = 0
            for let_t in t:
                if let_t == let:
                    rep_t_count += 1
                    if rep_t_count > rep_count:
                        return False
            if rep_t_count != rep_count:
                return False
        return True
