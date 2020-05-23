# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
import math

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1 
        end = n

        while start < end:
            middle = math.floor(start + end) // 2

            if not isBadVersion(middle):
                start = middle + 1
            else: 
                end = middle

        return start 