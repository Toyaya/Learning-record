#给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。
# 输入：haystack = "hello", needle = "ll"
# 输出：2
# haystack 和 needle 仅由小写英文字符组成

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            pos = haystack.find(needle)
            if pos != len(haystack):
                    return pos
            if haystack =='' and needle =='':
                    return 0
            else: 
                    return -1
#偷懒方法↑
# find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。


