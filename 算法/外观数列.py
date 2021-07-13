# 给定一个正整数 n ，输出外观数列的第 n 项。

# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1 
# 描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
# 描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
# 描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
# 描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"

# 核心思想：
# 创建慢指针和快指针 left、right 来确定每个字符的重复数量。

# 具体思路：

# 当 left 和 right 所指字符相同时，right 向右移动一位，直到 right 所指与 left 不同。
# 确定相同字符的个数，既 right - left 的值，该值表示的即是 left 所指字符的个数。
# 将结果转为以字符的形式储存。
# 继续历遍，因为 left 和 right 之间的字符已经历遍过了，所以更新指针 left 至 right。
# 当 right 超出字符范围时，结束循环。

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        res = self.countAndSay(n-1)
        left = 0
        right = 0
        new = ''
        length = len(res)
        for k in range(length):
            if res[left] != res[right]:
                new += str(right - left) + res[k-1]
                left = right
            right += 1
        new += str(right - left) + res[-1]
        return new

# JS：
# var countAndSay = function (n) {
#     if (n === 1) {
#         return "1";
#     };
#     let pre = countAndSay(n - 1);
#     let result = "", left = 0, right = 0;
#     while (right < pre.length) {
#         while (pre[left] === pre[right] && right < pre.length) {
#             right++;
#         };
#         result += (right - left).toString() + pre[left];
#         left = right;
#     }
#     return result;
# };


