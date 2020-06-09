class Solution:
    def isSubsequence(self, s, t):
        temp_pos = 0
        count = 0
        #print(len(s))
        for i in range(len(s)):
            for j in range(temp_pos,len(t)):
                if s[i] == t[j]:
                    temp_pos = j + 1
                    print(temp_pos)
                    count += 1
                    break
        if count == len(s):
            return True
        else:
            return False

answer = Solution().isSubsequence("axc", "ahbgdc")
print(answer)