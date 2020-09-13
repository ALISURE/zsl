"""
解题思路
此处撰写解题思路
思路：
1、采用bfs，则使用队列。
2、因为是无向图，防止走回头路，用visited来记录已走过的节点
3、要记录走过的路径/路径长度，因此用parent记录所走路径节点的上一个节点
4、关键是小蛇可以平移，因此将的状态分为2种，没种有3种行走方法
"""

class Solution:
    def minimumMoves(self, grid) -> int:
        directionH = [[0,0, 1, -1],[0,1,0,1],[1,0,1,0]]  # 蛇水平，前两位为尾巴，后两位为头部
        directionV = [[0,0, -1, 1],[0,1,0,1],[1,0,1,0]]  # 蛇竖直，前两位为尾巴，后两位为头部

        start = ((0, 0),(0, 1))  # （行，列）
        visited = set()
        visited.add(start)
        parent = {start: None}
        queue = [start]
        while queue:
            currPos = queue.pop(0)
            if currPos[0][0] == len(grid) - 1 and currPos[0][1] == len(grid[0]) - 2 and \
                    currPos[1][0] == len(grid) - 1 and currPos[1][1] == len(grid[0]) - 1:
                end = ((len(grid) - 1, len(grid[0]) - 2), (len(grid) - 1, len(grid[0]) - 1))
                num = -1
                while end != None:
                    num += 1
                    # print(end)
                    end = parent[end]
                print(num)
                # return parent
                return num

            if currPos[0][0] == currPos[1][0]:  # 蛇水平
                direction = directionH
            else:
                direction = directionV

            for item in direction:
                nextTail = (currPos[0][0] + item[0], currPos[0][1] + item[1])
                nextHead = (currPos[1][0] + item[2], currPos[1][1] + item[3])
