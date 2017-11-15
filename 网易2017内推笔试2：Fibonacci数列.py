'''
[编程题] Fibonacci数列
时间限制：1秒
空间限制：32768K
Fibonacci数列是这样定义的：
F[0] = 0
F[1] = 1
for each i ≥ 2: F[i] = F[i-1] + F[i-2]
因此，Fibonacci数列就形如：0, 1, 1, 2, 3, 5, 8, 13, ...，在Fibonacci数列中的数我们称为Fibonacci数。
给你一个N，你想让其变为一个Fibonacci数，每一步你可以把当前数字X变为X-1或者X+1，
现在给你一个数N求最少需要多少步可以变为Fibonacci数。 
输入描述:
输入为一个正整数N(1 ≤ N ≤ 1,000,000)


输出描述:
输出一个最小的步数变为Fibonacci数"

输入例子1:
15

输出例子1:
2
'''

'''
解题思路：这题简单，不解释
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''


n = int(input())
x = 0
y = 1

while y < n:
    x, y = y, x+y

print(min(y-n, n-x))
