class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        r_i = m - 1
        r_j = n - 1

        write_i = m + n - 1

        while r_j >= 0:
            if r_i >= 0 and nums1[r_i] > nums2[r_j]:
                nums1[write_i] = nums1[r_i]
                write_i -= 1
                r_i -= 1
            else:
                nums1[write_i] = nums2[r_j]
                write_i -= 1
                r_j -= 1
                
a = [0,0,3,0,0,0,0,0,0]
print(Solution().merge(a ,3,[-1,1,1,1,2,3],6), sep=", ")
print(a)
