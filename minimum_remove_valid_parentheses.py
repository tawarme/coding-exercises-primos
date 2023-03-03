class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_list = []

        stack = []
        for i in range(len(s)):
            ch = s[i]
            if ch not in "()":
                continue

            if ch == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    remove_list.append(i)

        remove_list.extend(stack)

        res = ""
        remove_list_i = 0
        for i in range(len(s)):
            if remove_list_i < len(remove_list) and i == remove_list[remove_list_i]:
                remove_list_i += 1
                continue
            res += s[i]

        return res
