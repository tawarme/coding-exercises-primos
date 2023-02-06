class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        median_ammount = (len(nums1) + len(nums2) + 1 )// 2
        #print(median_ammount)

        if len(nums1) < len(nums2):
            smaller = nums1
            bigger = nums2
        else:
            smaller = nums2
            bigger = nums1

        start = 0
        #end = median_pos
        end = len(smaller)
        #end = len(smaller) - 1
        #print(smaller)
        #print(bigger)

        while start <= end:
        #while True:
            #smaller_amount = start + end/2
            smaller_amount = (start + end) // 2
            bigger_amount = median_ammount - smaller_amount
            #print(smaller_amount, bigger_amount)

            smallerl = smaller[smaller_amount - 1] if smaller_amount else float("-inf")
            #smallerr = smaller[smaller_amount] if smaller_amount else float("inf")
            smallerr = smaller[smaller_amount] if smaller_amount != len(smaller) else float("inf")
            biggerl = bigger[bigger_amount - 1] if bigger_amount else float("-inf")
            biggerr = bigger[bigger_amount] if bigger_amount != len(bigger) else float("inf")

            if smallerl <= biggerr and biggerl <= smallerr:
                if (len(nums1) + len(nums2)) % 2 != 0:
                    #print("here A")
                    return max(smallerl, biggerl)
                else:
                    #print("here B")
                    return (max(smallerl, biggerl) + min(smallerr, biggerr)) / 2

            if smallerl > biggerr:
                #end = (start + end) // 2 + 1
                end = smaller_amount - 1
                continue

            if biggerl > smallerr:
                start = smaller_amount + 1
                #start = (start + end) // 2 - 1
                continue

