class Solution:
    def compareMemExpected(self, mem, expected):
        #print("comparing")
        if len(mem) != len(expected):
            return False

        for ch in expected:
            if mem.get(ch, 0) < expected[ch]:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        mem = {}
        expected = {}

        for ch in t:
            mem[ch] = 0
            expected[ch] = expected.get(ch, 0)
            expected[ch] += 1

        good_left = None
        good_right = 0

        left = 0
        right = 0

        criteria_needs = len(expected)
        criteria_count_match = 0

        ignore_right = False

        while left < len(s) and right < len(s):
            #print(mem)
            #print("eval", s[left:right+1], left, right)
            #if s[left] not in t:
            if expected.get(s[left]) is None:
                left += 1
                continue

            if right < left:
                right = left

            #if s[right] in t:
            if expected.get(s[right]) is not None:
                if not ignore_right:
                    mem[s[right]] += 1

                    if mem[s[right]] == expected[s[right]]:
                        criteria_count_match += 1

                ignore_right = False
                
                if criteria_count_match == criteria_needs:
                    if good_left is None or right - left < good_right - good_left:
                        good_right = right
                        good_left = left

                        #print("mod", good_left, good_right)

                    mem[s[left]] -= 1

                    if mem[s[left]] < expected[s[left]]:
                        criteria_count_match -= 1

                    left += 1
                    ignore_right = True
                    continue

            right += 1

        #print(good_left, good_right)
        if good_left is None:
            return ""

        return s[good_left:good_right + 1]
