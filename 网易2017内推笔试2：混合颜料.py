'''
[编程题] 混合颜料
时间限制：1秒
空间限制：32768K
你就是一个画家！你现在想绘制一幅画，但是你现在没有足够颜色的颜料。为了让问题简单，我们用正整数表示不同颜色的颜料。
你知道这幅画需要的n种颜色的颜料，你现在可以去商店购买一些颜料，但是商店不能保证能供应所有颜色的颜料，所以你需要自己混合一些颜料。
混合两种不一样的颜色A和颜色B颜料可以产生(A XOR B)这种颜色的颜料(新产生的颜料也可以用作继续混合产生新的颜色,XOR表示异或操作)。
本着勤俭节约的精神，你想购买更少的颜料就满足要求，所以兼职程序员的你需要编程来计算出最少需要购买几种颜色的颜料？ 
输入描述:
第一行为绘制这幅画需要的颜色种数n (1 ≤ n ≤ 50)
第二行为n个数xi(1 ≤ xi ≤ 1,000,000,000)，表示需要的各种颜料.


输出描述:
输出最少需要在商店购买的颜料颜色种数，注意可能购买的颜色不一定会使用在画中，只是为了产生新的颜色。

输入例子1:
3
1 7 3

输出例子1:
3
'''

'''
解题思路：把问题转换成矩阵求秩
  1、首先我们搞清楚什么是异或： 异或是一种位运算，若两个二进制数对应位的值不同，经过异或操作，得到1，否则得到0；
  例： 1 异或 0 = 1， 0异或0 = 1异或1 = 0  在python中用符号‘^’表示异或运算
  2、把需要的颜色从十进制转化为二进制数，并将所有颜色二进制数的位数都补全成颜色值最大的二进制，
  如例子中的1， 7， 3，转化为二进制后则为 001， 111， 011
  3、将每一个二进制数的当做矩阵的一个行，所有二进制数组成了一个矩阵
  例如：001， 111， 011，110 构成矩阵 0， 0， 1    接下来，利用高斯消元法求出矩阵秩即为需要购买的最少的颜料熟料，经过消元后，矩阵为 1， 1， 1， 
                                      1， 1， 1                                                                              0， 1， 1
                                      0， 1， 1                                                                              0， 0， 1
                                      1， 1， 0                                                                              0， 0， 0
  进一步消元可得：1， 0， 0  
                  0， 1， 0
                  0， 0， 1
                  0， 0， 0
  而原来的二进制数都可以由矩阵中非零行代表的二进制数经过异或得到，所以求最少的颜料数量就是求矩阵的秩

'''

'''
代码运行结果：
您的代码已保存
答案错误:您提交的程序没有通过所有的测试用例
case通过率为50.00%

测试用例:
31
60022292 120251010 43831590 431149545 96771213 13342066 6293394 132216816 36039549 49184271 459059174 66312582 7515945 427377819 433247867 508798489 11244256 432045760 462895764 95826852 469187846 507580066 94673695 81345284 12139099 127129817 68333174 471223030 1222843 477515108 429947218

对应输出应该为:

7

你的输出为:

26

用numpy求秩进行了验证，numpy求出来的秩也是26，查了好久，仍找不到问题在哪...
'''

n = int(input())
xn = sorted([int(each) for each in input().split()], reverse=True)
xn_bin = [[int(d) for d in bin(each)[2:]] for each in xn]
max_length = len(xn_bin[0])


for t in range(n):
    length_diff = len(xn_bin[t]) - max_length
    if length_diff < 0:
        xn_bin[t] = [0]*(-length_diff) + xn_bin[t]

for each in xn_bin:
    print(each)


def reduce(k, red1, red2):
    coefficient = red2[k] / red1[k]
    for m in range(k, max_length):
        red2[m] -= red1[m]*coefficient
    return red2


def count_zero(bin_vec):
    count_o = 0
    for each in bin_vec:
        if each == 0:
            count_o += 1
        else:
            break
    return count_o


def solve():
    benchmark = [None]*max_length
    for bit in range(max_length):
        for i in range(n):
            temp_o = count_zero(xn_bin[i])
            if temp_o == bit:
                if not benchmark[temp_o]:
                    benchmark[temp_o] = xn_bin[i]
                    xn_bin[i] = [0] * max_length
                    if benchmark.count(None) == 0:
                        return max_length
                else:
                    xn_bin[i] = reduce(bit, benchmark[bit], xn_bin[i])
    return max_length - benchmark.count(None)

print(solve())
