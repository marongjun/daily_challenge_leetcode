class Solution:
    def reverseString(self, s: List[str]) -> None:

        #solution 1
        tmp = s[::-1]
        for i in range(len(s)):
            s[i] = tmp[i]

        #solution 2
        i = 0
        j = len(s) - 1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
