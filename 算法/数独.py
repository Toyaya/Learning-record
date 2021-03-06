# 请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。



# 请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
# 输入：board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：true

# 想法很简单：
# 用r表示行，c表示列， 一个合格的数独只需要满足2个条件：

# 相同的数不能在同一个3x3区域，这个可以通过【r//3，c//3】来计算得到
# 相同的数不能在同一行或者列
# 所以只需要把数独转换成【行，列，区域】， 即【r, c, r//3, c//3】的图来进行比较就好了。

# 速度也很快

# python中的【//】是算术运算符号,表示取整除,它会返回结果的整数部分,例如【print(7//2)】,输出结果为3


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hashmap=dict()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if not val in hashmap: hashmap[val]=[[r, c, r//3, c//3]] # 没有收录就收录它
                    else: 
                        for old_r, old_c, zone_r, zone_c in hashmap[val]: # 收录了就比较它
                            if r//3 == zone_r and c//3 == zone_c: return False # 在同一区域
                            if r==old_r or c==old_c: return False # 在同一行或者列
                        hashmap[val].append([r, c, r//3, c//3]) # 更新哈希表
        return True