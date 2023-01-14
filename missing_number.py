class Solution:
    def missingNumber(self, nums: List[int]) -> int:



        # 11
        # 00
        # 01                    

        # for i in range(len(nums)+2):
        #     if i not in nums:
        #         return i      
        #print("  ", end= "")          
        #for i in range(len(nums),-1,  -1):
        #    print(i, end = "")
        #print("")
        # num_reg = 0
        # for num in nums:
        #     num_reg |= 1 << num 
        #     #print(bin(num_reg), num)
        # #print(bin(num_reg))
        # mask = (1 << (len(nums)+1))-1
        # #print(bin(num_reg ^ mask))
        # mask = num_reg ^ mask

        # x = 0
        # while mask:
        #     mask >>= 1
        #     x += 1
        # return x-1

        xor_test = 0
        for i in range(len(nums)):
            xor_test ^= (nums[i] ^ i)
        xor_test ^= len(nums)

        return xor_test