'''
[编程题] 两种排序方法
时间限制：1秒
空间限制：32768K
考拉有n个字符串字符串，任意两个字符串长度都是不同的。考拉最近学习到有两种字符串的排序方法： 1.根据字符串的字典序排序。例如：
"car" < "carriage" < "cats" < "doggies < "koala"
2.根据字符串的长度排序。例如：
"car" < "cats" < "koala" < "doggies" < "carriage"
考拉想知道自己的这些字符串排列顺序是否满足这两种排序方法，考拉要忙着吃树叶，所以需要你来帮忙验证。 
输入描述:
输入第一行为字符串个数n(n ≤ 100)
接下来的n行,每行一个字符串,字符串长度均小于100，均由小写字母组成


输出描述:
如果这些字符串是根据字典序排列而不是根据长度排列输出"lexicographically",

如果根据长度排列而不是字典序排列输出"lengths",

如果两种方式都符合输出"both"，否则输出"none"

输入例子1:
3
a
aa
bbb

输出例子1:
both
'''

'''
解题思路：两种方法的思路都很简单，不过多阐述。
  至于第二种排序，python内置函数sorted即可实现，在这儿我自己写代码重新实现了一遍
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n = int(input())
strings = [input() for i in range(n)]

strings_length = [len(each) for each in strings]

if sorted(strings_length) == strings_length:
    lengths = True
else:
    lengths = False


def judge(strings_test):
    for i in range(n-1):
        temp_len = len(strings_test[i])
        for j in range(temp_len):
            ord1 = ord(strings_test[i][j])
            try:
                ord2 = ord(strings_test[i+1][j])
            except IndexError:
                return False
            if ord1 > ord2:
                return False
            elif ord1 < ord2:
                break
    return True

lexicographically = judge(strings)

if lexicographically:
    if lengths:
        print('both')
    else:
        print('lexicographically')
elif lengths:
    print('lengths')
else:
    print('none')
