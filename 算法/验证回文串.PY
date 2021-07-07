# （双指针）

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。

# 示例 1:
# 输入: "A man, a plan, a canal: Panama"
# 输出: true


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())  #.lower()转成小写      .isalnum()检测字符串是否由字母和数字组成 
        n = len(sgood)
        left, right = 0, n - 1
        
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True

# 复杂度分析

# 时间复杂度：O(|s|)O(∣s∣)，其中 |s|∣s∣ 是字符串 ss 的长度。

# 空间复杂度：O(|s|)O(∣s∣)。由于我们需要将所有的字母和数字字符存放在另一个字符串中，在最坏情况下，新的字符串 \textit{sgood}sgood 与原字符串 ss 完全相同，因此需要使用 O(|s|)O(∣s∣) 的空间。

