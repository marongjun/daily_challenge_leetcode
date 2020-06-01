def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        key_val = None
        for key, value in dic.items():
            if value == 1:
                key_val = key
        return key_val
import time
def isHappy( n):
        """
        :type n: int
        :rtype: bool
        """
        m_set = []
        while n:
            if n != 1:
                digits = []
                temp = n
                power = 10
                while True:
                    if temp!=0:
                        digits.append(temp%power)
                        temp = temp // power
                    else:
                        break
                n = 0
                for digit in digits:
                    n += digit **2
                print(n, digits)
                if n in m_set:
                    return False
                else:
                    m_set.append(n)
                time.sleep(0.5)
            elif n == 1:
                return True


answer = singleNumber([2,2,1])
happy = isHappy(2)
print(happy)