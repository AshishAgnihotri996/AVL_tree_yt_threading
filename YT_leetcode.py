class Solution:
    def longestPrefixCommon(self,strs):
        if len(strs) == 0:
            return False

        minlen = len(strs[0])
        for i in range(len(strs)):
            minlen = min(len(strs),minlen)

        lcp = " "
        i = 0
        while i < minlen:
            char = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != char:
                    return lcp
            lcp = lcp + char
            i+=1
        print(lcp)



s = Solution()
s.longestPrefixCommon(['flower','flow','flight'])




