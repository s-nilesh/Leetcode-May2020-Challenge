#PROBLEM
#Given a positive integer num, write a function which returns True if num is a perfect square else False.
#Note: Do not use any built-in library function such as sqrt.

#Example 1:
#Input: 16
#Output: true

#Example 2:
#Input: 14
#Output: false





#SOLUTION-1  (BEST)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<0:
            return False
        elif (num == 1) or (num == 0):
            return True
        s = (len(str(num))-1) // 2
        x = (10**s) * 4

        A = {x, num}
        while x * x != num:
            x = (x + (num // x)) >> 1
            if x in A:
                return False
            A.add(x)
        return True



#SOLUTION-2
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<0:
            return False
        elif (num == 1) or (num == 0):
            return True
        x = num // 2
        seen = set([x])
        while x * x != num:
            x = (x + (num // x)) // 2
            if x in seen:
                return False
            seen.add(x)
        return True


#SOLUTION-3
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<0:
            return False
        elif (num == 1) or (num == 0):
            return True
	i = 1
        while i**2 <= num:
            if num/i == i:
                return True
            i += 1
        return False
