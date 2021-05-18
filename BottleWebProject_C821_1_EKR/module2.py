from bottle import post, request
import re
import pdb
import json
import random
@post ('/var2', method = 'post')
def vglubiny():
    #алгоритм в глубину
    def dfs(graph, node, visited):
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                dfs(graph,n, visited)
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

    #запуск алгоритма в глубину
    visited = dfs(graph0,'1', [])

    #вывод
    final_output="Случайносгенерированный словарь смежности вершин:  <br>  " + str(graph0) + " <br><br> Порядок обхода: <br> " + str(visited) + ""
    return(final_output)
