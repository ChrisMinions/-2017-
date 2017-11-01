'''
[编程题] 解救小易
时间限制：1秒
空间限制：32768K
有一片1000*1000的草地，小易初始站在(1,1)(最左上角的位置)。
小易在每一秒会横向或者纵向移动到相邻的草地上吃草(小易不会走出边界)。
大反派超超想去捕捉可爱的小易，他手里有n个陷阱。
第i个陷阱被安置在横坐标为xi ，纵坐标为yi 的位置上，小易一旦走入一个陷阱，将会被超超捕捉。
你为了去解救小易，需要知道小易最少多少秒可能会走入一个陷阱，从而提前解救小易。 
输入描述:
第一行为一个整数n(n ≤ 1000)，表示超超一共拥有n个陷阱。
第二行有n个整数xi，表示第i个陷阱的横坐标
第三行有n个整数yi，表示第i个陷阱的纵坐标
保证坐标都在草地范围内。


输出描述:
输出一个整数,表示小易最少可能多少秒就落入超超的陷阱

输入例子1:
3
4 6 8
1 2 1

输出例子1:
3
'''

'''
解题思路：广度优先搜索算法（bfs）
  1、先遍历初始点集合，判断集合中的点上是否有陷阱，若有陷阱，返回0；若无，则把初始点放入已经搜索过的点的集合searched。
  利用get_neighbor函数得到初始点集合附近的点，附近的点不能超过边界，也不能在searched中，将函数返回的集合放入待搜索点集合中
  2、遍历结束后，如果待搜索点集合非空，则对其进行递归bfs搜索，若递归bfs返回值为-1，表示搜索失败，继续返回-1，若返回值
  不是-1，则返回 1+返回值 表示步数
  3、若待搜索集合为空，表示所有点都遍历完，未发现陷阱，搜索失败，返回-1
'''

'''
代码运行结果：
您的代码已保存
内存超限:您的程序使用了超过限制的内存
case通过率为90.00%
'''

n = int(input())

x_cords = [int(each) for each in input().split()]
y_cords = [int(each) for each in input().split()]
traps = [(x_cords[i], y_cords[i]) for i in range(n)]


def get_neighbor(pos):
    neighbor = set()
    if pos[0] + 1 < 1000 and (pos[0]+1, pos[1]) not in searched:
        neighbor.add((pos[0]+1, pos[1]))
    if pos[1] + 1 < 1000 and (pos[0], pos[1]+1) not in searched:
        neighbor.add((pos[0], pos[1]+1))
    return neighbor


def bfs(current_list):
    wait_list = set()
    for each in current_list:
        if each in traps:
            return 0
        else:
            searched.add(each)
            wait_list.update(get_neighbor(each))
    if wait_list:
        temp = bfs(wait_list)
        if temp != -1:
            return 1 + temp
    else:
        return -1

searched = set()
init_pos = set()
init_pos.add((1, 1))
print(bfs(init_pos))
