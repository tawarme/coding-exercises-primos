# TODO: Review in the future for better solution

class Solution(object):
    def facto(self, x):
        fact = 1
        for x in range(1, x+1):
            fact = fact*x
        return fact

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_move_steps = n
        min_move_steps = round(n/2, 1)
        max_moves = n

        total_moves = max_move_steps
        two_step_moves = 0
        cumulated_moves = 0
        while total_moves >= min_move_steps:
            total_moves = total_moves - two_step_moves
            
            one_step_moves = total_moves - two_step_moves

            cumulated_moves += (self.facto(total_moves)/(self.facto(one_step_moves)*self.facto(two_step_moves)))

            two_step_moves += 1

        return cumulated_moves
