// https://leetcode.com/problems/maximum-running-time-of-n-computers

class Solution:
    '''
    Sort and take the largest n batteries.
    
    Example
    num computers:   4
    Largest 4:       1 3 6 10
    Batteries:       a b c d  ...

    The min of the largest n is the limiting. i.e. battery a.
    Since swapping takes 0 time, any and all of the remaining can be used to "top up" (by swapping out) batt a to the same time as batt b.
    Once a is topped up, then a+b needs to be topped up to c.
    If at any point in time there is not enough to top up to next threshold, then split accordingly.
    '''

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # number of batteries
        numbat = len(batteries)

        # if fewer batt than comp, then cannot run simultaneous
        if n > numbat:
            return 0

        # equal num of batteries, no need to check
        # to check later if can be subsumed into algo
        if n == numbat:
            return min(batteries)

        # largest at the back. nlogn time, constant space
        batteries.sort()

        # since swapping is free, the extras is used to just top up
        # n time, constant space
        extra = sum(batteries[i] for i in range(numbat - n))

        # iterate over the n largest batt, starting from the smallest
        # i is also the num of batteries that has been topped up,
        # hence range is from 1 to n + 1
        # to compensate, the current battery looked at is -n - 1 + i
        # n time, constant space
        for i in range(1, n + 1):
            # runtime of the current battery looked at
            runtime = batteries[-n - 1 + i]
            # last battery has nothing to compare to, so just split
            if i == n:
                return self.split_remaining(extra, i, runtime)
            
            # compare with the next larger battery
            diff = batteries[-n - 1 + i + 1] - batteries[-n - 1 + i]
            
            # if can top up this and all the computers before, top up
            # if diff is 0, alr accounted for and move on
            if extra >= diff * i:
                extra -= diff * i
            else:
                return self.split_remaining(extra, i, runtime)

    '''
    split remaining extra battery span
    '''
    def split_remaining(self, extra: int, num: int, runtime: int) -> int:
        # do integer division
        return runtime + extra // num




