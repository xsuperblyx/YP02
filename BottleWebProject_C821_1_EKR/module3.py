from bottle import post, request
import re
import pdb
import json
import random
from collections import defaultdict
@post ('/var3', method = 'post')

#метод крускала
def kraskal():
    class UnionFind:
        def __init__(self,val,leader):
            self.val = val
            self.leader = leader
        def changeLeader(self,leader):
            self.leader = leader

        def returnLeader(self):
            return self.leader


    def kruskal(graph,edges, N):
        T = dict()
        sizes = defaultdict(lambda: 0)
        edgeWeights = []

        for indx, edge in enumerate(edges):
            n1 = graph[edge][0]
            n2 = graph[edge][1]
            if (n1.leader == n2.leader):
                pass

            elif (n1.leader in T.keys()) and (n2.leader not in T.keys()):
                n2.changeLeader(n1.leader)
                T[n1.leader].append(n2)
                sizes[n1.leader] += 1
                edgeWeights.append(edge)

            elif (n2.leader in T.keys()) and (n1.leader not in T.keys()):
                n1.changeLeader(n2.leader)
                T[n2.leader].append(n1)
                sizes[n2.leader] += 1
                edgeWeights.append(edge)

            elif (n1.leader in T.keys()) and (n2.leader in T.keys()) and (n1.leader != n2.leader):
                size1 = sizes[n1.leader]
                size2 = sizes[n2.leader]
                edgeWeights.append(edge)
                if size1 >= size2:
                    for node in T[n2.leader]:
                        if node is not n2:
                            node.changeLeader(n1.leader)
                            T[n1.leader].append(node)
                            sizes[n1.leader] += 1
                            sizes[n2.leader] -= 1
                    del T[n2.leader]
                    sizes[n2.leader] = 0
                    n2.changeLeader(n1.leader)
                    T[n1.leader].append(n2)
                else:
                    for node in T[n1.leader]:

                        if node is not n1:
                            node.changeLeader(n2.leader)
                            T[n2.leader].append(node)
                            sizes[n2.leader] += 1
                            sizes[n1.leader] -= 1

                    del T[n1.leader]
                    sizes[n1.leader] = 0
                    n1.changeLeader(n2.leader)
                    T[n2.leader].append(n1)
            else:
                n2.changeLeader(n1.leader)
                T[n1.leader] = [n1,n2]
                sizes[n1.leader] +=2
                edgeWeights.append(edge)
        for node in T['A']:
            nodeval=node.val
        out=(nodeval,"<br>",T,"<br>",edgeWeights)
        return (out)

    nodes = [UnionFind("A","A"),UnionFind("B","B"),UnionFind("C","C"),UnionFind("D","D"),UnionFind("E","E")]

    #генерация словаря смежности вершин
    i=random.randint(1,5)
    if i==1:
        graph0 = {'1': ['2', '3'], '2': ['1','4', '5'], '3': ['1','5'], '4':['2','5'], '5':['2','3','4']} 
        mtrx=[[0,1,1,0,0],[1,0,0,1,1],[1,0,0,0,1],[0,1,0,0,1],[0,1,1,1,0]]
    elif i==2:
        graph0 = {'1': ['2', '3'], '2': ['1','3'], '3': ['1','2']} 
        mtrx=[[0,1,1],[1,0,1],[1,1,0]]
    elif i==3:
        graph0 = {'1': ['2', '3'], '2': ['1','3'], '3': ['1','2','4'], '4': ['3']} 
        mtrx=[[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]
    elif i==4:
        graph0 = {'1': ['2', '3'], '2': ['1','3','4','5'], '3': ['1','2'], '4': ['2','5'], '5': ['2','4','6'], '6': ['5']} 
        mtrx=[[0,1,1,0,0,0],[1,0,1,1,1,0],[1,1,0,0,0,0],[0,1,0,0,1,0],[0,1,0,1,0,1],[0,0,0,0,1,0]]
    elif i==5:
        graph0 = {'1': ['2', '3', '4'], '2': ['1', '3', '4'], '3': ['1','2','4'], '4':['1','2','3']} 
        mtrx=[[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]

    N = 5
    edges = list(graph0.keys())
    edges.sort()

    #запуск и вывод
    krask = kruskal(graph0,edges,N)
    return (krask)