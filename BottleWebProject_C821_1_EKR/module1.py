from bottle import post, request
import re
import pdb
import json
import random
@post ('/var1', method = 'post')
def vshiriny():
    #алгоритм в ширину
    def bfs(visited,graph,node):
        queue = []
        visited.append(node)
        queue.append(node)
        while queue:
            s = queue.pop(0)
            for neighbor in graph[s]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return(visited)

    #генерация словаря смежности вершин
    i=random.randint(1,5)
    if i==1:
        graph0 = {'1': ['2', '3'], '2': ['1','4', '5'], '3': ['1','5'], '4':['2','5'], '5':['2','3','4']} 
    elif i==2:
        graph0 = {'1': ['2', '3'], '2': ['1','3'], '3': ['1','2']} 
    elif i==3:
        graph0 = {'1': ['2', '3'], '2': ['1','3'], '3': ['1','2'], '4': ['4']} 
    elif i==4:
        graph0 = {'1': ['2', '3'], '2': ['1','3','4','5'], '3': ['1','2'], '4': ['2','5'], '5': ['2','4'], '6': ['5']} 
    elif i==5:
        graph0 = {'1': ['2', '3', '4'], '2': ['1', '3', '4'], '3': ['1','2','4'], '4':['1','2','3']} 

    #запуск алгоритма в ширину
    visited = bfs([],graph0, '1')

    #вывод
    final_output="Случайносгенерированный словарь смежности вершин:  <br>  " + str(graph0) + " <br><br> Порядок обхода: <br> " + str(visited) + ""
    return(final_output)



