'''
[编程题] 幸运的袋子
时间限制：1秒
空间限制：32768K
一个袋子里面有n个球，每个球上面都有一个号码(拥有相同号码的球是无区别的)。
如果一个袋子是幸运的当且仅当所有球的号码的和大于所有球的号码的积。
例如：如果袋子里面的球的号码是{1, 1, 2, 3}，这个袋子就是幸运的，因为1 + 1 + 2 + 3 > 1 * 1 * 2 * 3
你可以适当从袋子里移除一些球(可以移除0个,但是别移除完)，要使移除后的袋子是幸运的。
现在让你编程计算一下你可以获得的多少种不同的幸运的袋子。 
输入描述:
第一行输入一个正整数n(n ≤ 1000)
第二行为n个数正整数xi(xi ≤ 1000)


输出描述:
输出可以产生的幸运的袋子数

输入例子1:
3
1 1 1

输出例子1:
2
'''

'''
解题思路：深度优先搜索算法（dfs）
  1、将输入的数组按从小到大的顺序进行重排
  2、数出数列中1个个数，存放在num_1中，按1的个数递增的顺序进行循环，明显数组中前num_1个数都是1
  3、对不同的1的个数，都进行递归dfs，递归结束的条件（1）遍历完数组 （2）遍历过程中袋子不满足幸运的条件
  把满足幸运条件的组合都放入集合results中（使用集合避免重复解）
        dfs实现：从数列中的地num_1+1个数（即第一个非1的数）开始，将这个数和已有的1组合成袋子，观察其是否满足幸运的条件
        如果满足，将袋子的情况保存进results中，递归dfs，直至不满足幸运的条件
'''

'''
代码运行结果：
您的代码已保存
内存超限:您的程序使用了超过限制的内存
case通过率为80.00%
'''

n = int(input())
xn = sorted([int(each) for each in input().split()])


def mul(other):
    product = 1
    if other:
        for each in other:
            product *= each
        return product
    else:
        return 1


def dfs(num1, current, num):
    if num == n:
        return
    else:
        for j in range(num, n):
            if xn[j] + num1 + sum(current) > mul(current) * xn[j]:
                temp = current + (xn[j],)
                results.add((1,) * num1 + temp)
                dfs(num1, temp, j+1)
            else:
                return
num_1 = xn.count(1)
results = set()
for i in range(1, num_1+1):
    dfs(i, (), num_1)

length = len(results)
if length == 0:
    print(num_1 - 1)
else:
    print(length + num_1 - 1)
