# class Solution:
#     def longestPrefixCommon(self,strs):
#         if len(strs) == 0:
#             return False
#
#         minlen = len(strs[0])
#         for i in range(len(strs)):
#             minlen = min(len(strs),minlen)
#
#         lcp = " "
#         i = 0
#         while i < minlen:
#             char = strs[0][i]
#             for j in range(1,len(strs)):
#                 if strs[j][i] != char:
#                     return lcp
#             lcp = lcp + char
#             i+=1
#         print(lcp)
#
#
#
# s = Solution()
# s.longestPrefixCommon(['flower','flow','flight'])
#
#
# 50

# class Solution:
#     def removeKdigits(self,num,k):
#         stack = []
#         remove_k_digits = k
#         for curr_element in num :
#             while remove_k_digits and stack and stack[-1] > curr_element:
#                 stack.pop()
#                 remove_k_digits = remove_k_digits -1
#             stack.append(curr_element)
#         ans = " ".join(stack[0:len(num)-k]).lstrip("0")
#         if len(ans):
#             return ans
#         else:
#             return "0"
#
