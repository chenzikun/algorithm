#!/usr/bin/env
# encoding: utf-8
"""
-------------------------------------------------
    date:          2022-04-17   
    Author:       chenzikun         
-------------------------------------------------

"""
from copy import deepcopy       #复制模块（深复制）
class cycle(object):
    def __init__(self,Graph):
        self.Graph = Graph
        self.path = []
        self.all_path = {}
        self.marked = []
        self.edge = 0
        for i in range(len(self.Graph)):
            self.marked.append(0)

    #计算顶点的度数
    def degree(self,v):
        self.Degree = len(self.Graph[str(v)])
        return self.Degree

    #稍稍改变的深度优先搜索方法
    def DFS(self,vote):
        self.vote = vote
        if self.marked[int(self.vote)] == 1:
            return
        else:
            self.marked[int(self.vote)] = 1
            self.path.append(int(self.vote))
        for i in self.Graph[str(self.vote)]:
            self.DFS(i)

    # 判断无向图是否有环或者无环
    def cy(self):
        self.n = len(self.Graph)        #存储图的顶点数
        for value in self.Graph.values():   #计算图的总边数
           self.edge = self.edge+len(value)
        self.edge = self.edge//2
        print(self.n)
        if self.edge >= self.n:     #此为边edge大于等于顶点时
            print("给定无向图是一个有环图")
        else:          #边数小于顶点时候的处理算法（不断的删除顶点度小于等于1的顶点和含有此顶点的边）
            self.New_Graph = deepcopy(self.Graph)
            for t in range(self.edge+self.n):   #循环的最多次数为边数+顶点数
                for k,v in self.Graph.items():
                    if self.degree(k) <=1:
                        del self.New_Graph[k]
#                        print(self.New_Graph)
                        for p,q in self.Graph.items():
                            if int(k) in q:
                                self.New_Graph[p].remove(int(k))
#                                print(k,q,self.New_Graph)
                self.Graph = deepcopy(self.New_Graph)

            if len(self.Graph) > 0:   #如果循环完毕其图还存在点，则为有环图，反之无环图
                print("给定无向图是一个有环图")
            else:
                print("给定无向图是一个无环图")



if __name__ == '__main__':
    Graph = {'0':[5,1],
             '1':[0],
             '3':[4],
             '4':[5,6,3, 0],
             '5':[4,0],
             '6':[4],
             }
    g=cycle(Graph)
    g.cy()

