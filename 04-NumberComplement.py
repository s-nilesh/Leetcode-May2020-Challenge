#PROBLEM
#Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

#Example 1:
#Input: 5
#Output: 2
#Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

#Example 2:
#Input: 1
#Output: 0
#Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

#Note:
#The given integer is guaranteed to fit within the range of a 32-bit signed integer.
#You could assume no leading zero bit in the integer’s binary representation.





#SOLUTION-1
class Solution:
    def intToBinCompString(self, intVal: int) -> str:
        """
        Takes interger value as an input.
        Returns Complement of binary value of the given interger 
        """
        if intVal == 0: 
            return "1" 
        strVal = "" 
        while intVal > 0: 
            if intVal%2 != 0: 
                strVal = "0" + strVal 
            else: 
                strVal = "1" + strVal 
            intVal = intVal//2 
        return strVal 
    def binaryToInt(self, binVal: str) -> int: 
        """
        Takes in binary representation as string.
        Returns base-10 number of given binary
        """
        intVal = 0 
        for i,val in enumerate(binVal[::-1]): 
            if val == '1': 
                intVal = intVal + (2**i) 
        return intVal 
    def findComplement(self, num: int) -> int:
        return self.binaryToInt(self.intToBinCompString(num))


#SOLUTION-2
class Solution:
    def findComplement(self, num: int) -> int:
        binVal = f'{num:b}'
        binComplement = ''.join(['0' if x=='1' else '1' for x in binVal])
        return int(binComplement, 2)



#SOLUTION-3 (best solution)
class Solution:
    def findComplement(self, num: int) -> int:
        return ((1 << int(math.log(num,2)) + 1) - 1) ^ num
#first we found number of bits required to represent num in binary. Then we created a binary representation of all 1 of the same number of bits. After that we preformed bitwise xor of given number with our generated number to get complement of the number. Efficient use of bitwise operators in python
