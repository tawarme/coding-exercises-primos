class Solution:
    def decode(self, enc_str):
        strs = []

        while enc_str:
            lenght, enc_str = enc_str.split(":", 1)
            lenght = int(lenght)
            strs.append(enc_str[:lenght])
            enc_str = enc_str[lenght:]
        return strs


    def encode(self, strs):
        enc_str = ""

        for s in strs:
            enc_str += str(len(s)) + ":"
            enc_str += s

        return enc_str


if __name__ == "__main__":
    tests = [
                [["hello", "world"], ["hello", "world"]],
            ]

    for test in tests:
        ans = test[0]
        sol = Solution()
        assert sol.decode(sol.encode(*test[1:])) == ans
