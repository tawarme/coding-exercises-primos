class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(1, n + 1):
            ansstr = ""
            if i % 3 == 0:
                ansstr = "Fizz"

            if i % 5 == 0:
                ansstr += "Buzz"
            
            if ansstr:
                answer.append(ansstr)
            else:
                answer.append(str(i))

        return answer
