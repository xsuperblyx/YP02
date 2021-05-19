from bottle import post, request
import re
import pdb
import json
import random
from collections import defaultdict
@post ('/var3', method = 'post')

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

#           print("edge is", edge,"nodes",n1.val,n2.val,"leaders",n1.leader,n2.leader)
#           print("state of dict is", T.keys())
            if (n1.leader == n2.leader):
#                 print("both nodes part of",n1.leader,'do nothing \n')
                pass

            elif (n1.leader in T.keys()) and (n2.leader not in T.keys()):
#               print("adding ",n2.val, "to group",n1.leader,'\n')
                n2.changeLeader(n1.leader)
                T[n1.leader].append(n2)
                sizes[n1.leader] += 1
                edgeWeights.append(edge)

            elif (n2.leader in T.keys()) and (n1.leader not in T.keys()):
#               print("adding ",n1.val, "to group",n2.leader,'\n')

                n1.changeLeader(n2.leader)
                T[n2.leader].append(n1)
                sizes[n2.leader] += 1
                edgeWeights.append(edge)

            elif (n1.leader in T.keys()) and (n2.leader in T.keys()) and (n1.leader != n2.leader):
#               print("merging groups",n1.leader,n2.leader)
                size1 = sizes[n1.leader]
                size2 = sizes[n2.leader]
                edgeWeights.append(edge)

#             print("sizes are",size1, size2)
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

#                 print("updated list of nodes",T.keys())
#                 for node in T[n1.leader]:
#                     print("includes",node.val)
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
#               print("adding new group",n1.val,n2.val,'\n')
                n2.changeLeader(n1.leader)
                T[n1.leader] = [n1,n2]
                sizes[n1.leader] +=2
                edgeWeights.append(edge)

#               print("updated nodes",graph[edge][0].val,graph[edge][1].val,"leaders",
#               graph[edge][0].leader,graph[edge][1].leader,"\n")
        for node in T['A']:
            nodeval=node.val
        out=(nodeval,"<br>",T,"<br>",edgeWeights)
        return (out)

    nodes = [UnionFind("A","A"),UnionFind("B","B"),UnionFind("C","C"),UnionFind("D","D"),UnionFind("E","E")]
    graph = {1:[nodes[0],nodes[1]],2:[nodes[3],nodes[4]],
            3:[nodes[0],nodes[4]],4:[nodes[0],nodes[3]],
            5:[nodes[0],nodes[2]],6:[nodes[2], nodes[4]],
            7:[nodes[1],nodes[2]]}
    N = 5
    edges = list(graph.keys())
    edges.sort()

    krask = kruskal(graph,edges,N)
    return (krask)