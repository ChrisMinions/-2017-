'''
[编程题] 小易喜欢的单词
时间限制：1秒
空间限制：32768K
小易喜欢的单词具有以下特性：
1.单词每个字母都是大写字母
2.单词没有连续相等的字母
3.单词没有形如“xyxy”(这里的x，y指的都是字母，并且可以相同)这样的子序列，子序列可能不连续。
例如：
小易不喜欢"ABBA"，因为这里有两个连续的'B'
小易不喜欢"THETXH"，因为这里包含子序列"THTH"
小易不喜欢"ABACADA"，因为这里包含子序列"AAAA"
小易喜欢"A","ABA"和"ABCBA"这些单词
给你一个单词，你要回答小易是否会喜欢这个单词。 
输入描述:
输入为一个字符串，都由大写字母组成，长度小于100


输出描述:
如果小易喜欢输出"Likes",不喜欢输出"Dislikes"

输入例子1:
AAA

输出例子1:
Dislikes
'''

'''
解题思路：动态规划
  条件二判断很简单，不阐述
  条三件判断：
  1、遍历取出字符串前n-2位子串中任意一个长度为2的子串1，根据子串1中第二个字母的位置，把字符串切割该字母前（包括该字母）
  和该字母后两部分，取后一部分记为子串2
  2、利用动态规划计算子串1和子串2公共子串的长度，若长度为2，则不满足条件三。 动态规划部分可参见《算法图解》一书
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''


string = input()
length = len(string)


def condition1(s):
    for i in range(length-1):
        if s[i] == s[i+1]:
            return False
    return True


def condition2(s):
    def judge(s1, s2):
        temp_len = len(s2)
        dp = [0]*(temp_len+1)
        for each in s1:
            dp_ = [0]*(temp_len+1)
            for bit in range(temp_len):
                if each == s2[bit]:
                    dp_[bit+1] = dp[bit] + 1
                else:
                    dp_[bit+1] = max(dp_[bit], dp[bit+1])
            dp = dp_
        if dp[temp_len] == 2:
            return False
        else:
            return True
    for i in range(1, length-2):
        for j in range(i):
            if not judge(s[j]+s[i], s[i+1:]):
                return False
    return True

if condition1(string) and condition2(string):
    print('Likes')
else:
    print('Dislikes')
