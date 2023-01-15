# TODO: REVIEW AND TRANSFORM to space O(1)
class Solution(object):
    def productExceptSelf(self, nums):
        answer_l = []
        answer_r = []
        for i in range(len(nums)):
            #print(answer_l)
            if not i:
                answer_l.append(1)
                answer_r.append(1)
            else:
                #answer[i] = answer[i-1]*nums[i-1]
                answer_l.append(answer_l[i-1]*nums[i-1])
                answer_r.append(answer_r[i-1]*nums[((len(nums) - 1) - i) +1])

        answer = []

        for i in range(len(nums)):
            answer.append(answer_l[i] * answer_r[len(nums) - 1 - i])
            #print(answer)
        return answer
