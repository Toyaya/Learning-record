#给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# s = "leetcode"
# 返回 0

# s = "loveleetcode"
# 返回 2
 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for x in s:
            if s.find(x) == s.rfind(x):
                return s.find(x)
        return -1
 

# rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
# find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

