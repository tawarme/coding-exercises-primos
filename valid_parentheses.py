class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        oposites = {"(":")", "[":"]", "{":"}"}
        parentheses_closure = ")]}"
        parentheses_stack = []
        for par in s:
            #print("Par", par)
            #print("Par stack")
            #print(parentheses_stack)
            if parentheses_stack:
                if par != parentheses_stack[-1]:
                    if par in parentheses_closure:
                        return False
                else:
                    parentheses_stack.pop(-1)
                    continue
            else:
                if par in parentheses_closure:
                    return False
            parentheses_stack.append(oposites[par])
            #print("********************")

        return len(parentheses_stack) == 0
