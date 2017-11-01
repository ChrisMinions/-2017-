'''
[编程题] 不要二
时间限制：1秒
空间限制：32768K
二货小易有一个W*H的网格盒子，网格的行编号为0~H-1，网格的列编号为0~W-1。
每个格子至多可以放一块蛋糕，任意两块蛋糕的欧几里得距离不能等于2。
对于两个格子坐标(x1,y1),(x2,y2)的欧几里得距离为:
( (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) ) 的算术平方根
小易想知道最多可以放多少块蛋糕在网格盒子里。 
输入描述:
每组数组包含网格长宽W,H，用空格分割.(1 ≤ W、H ≤ 1000)


输出描述:
输出一个最多可以放的蛋糕数

输入例子1:
3 2

输出例子1:
4
'''

'''
解题思路：这题不难，只要仔细的区分清楚各种特殊情况，小心设置if的条件即可得到答案
  0 1 2 3 4 5 6 7
0 X X     X X
1 X X     X X
2     X X     X X 
3     X X     X X
4 X X     X X 
5 X X     X X
6     X X     X X
7     X X     X X
按这种情况放置的蛋糕是最合理的
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

W, H = [int(each) for each in input().split()]

mod_column = W % 4
mod_row = H % 4

column_block = W // 4
row_block = H // 4

if mod_column == 0:
    print((8 * column_block) * row_block + 2 * column_block * mod_row)
elif mod_column == 1:
    if 0 < mod_row <= 2:
        print((8 * column_block + 2) * row_block + (2 * column_block + 1) * mod_row)
    elif mod_row == 3:
        print((8 * column_block + 2) * row_block + (2 * column_block + 1) * 2 + 2 * column_block)
    else:
        print((8 * column_block + 2) * row_block)
elif mod_column == 2:
    if 0 < mod_row <= 2:
        print((8 * column_block + 4) * row_block + (2 * column_block + 2) * mod_row)
    elif mod_row == 3:
        print((8 * column_block + 4) * row_block + (2 * column_block + 2) * 2 + 2 * column_block)
    else:
        print((8 * column_block + 4) * row_block)
elif mod_column == 3:
    if 0 < mod_row <= 2:
        print((8 * column_block + 6) * row_block + (2 * column_block + 2) * mod_row)
    elif mod_row == 3:
        print((8 * column_block + 6) * row_block + (2 * column_block + 2) * 2 + 2 * column_block + 1)
    else:
        print((8 * column_block + 6) * row_block)
