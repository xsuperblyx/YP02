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
        mtrx=[[0,1,1,0,0],[1,0,0,1,1],[1,0,0,0,1],[0,1,0,0,1],[0,1,1,1,0]]
        gr='gr1'
    elif i==2:
        graph0 = {'1': ['2', '3'], '2': ['1','3'], '3': ['1','2']} 
        mtrx=[[0,1,1],[1,0,1],[1,1,0]]
        gr='gr2'
    elif i==3:
        graph0 = {'1': ['2', '3'], '2': ['1','3'], '3': ['1','2','4'], '4': ['3']} 
        mtrx=[[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]
        gr='gr3'
    elif i==4:
        graph0 = {'1': ['2', '3'], '2': ['1','3','4','5'], '3': ['1','2'], '4': ['2','5'], '5': ['2','4','6'], '6': ['5']} 
        mtrx=[[0,1,1,0,0,0],[1,0,1,1,1,0],[1,1,0,0,0,0],[0,1,0,0,1,0],[0,1,0,1,0,1],[0,0,0,0,1,0]]
        gr='gr4'
    elif i==5:
        graph0 = {'1': ['2', '3', '4'], '2': ['1', '3', '4'], '3': ['1','2','4'], '4':['1','2','3']} 
        mtrx=[[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
        gr='gr5'

    #прием переменных, введенных с клавиатуры на вкладке данного метода
    strt1=request.forms.get('START1')

    #запуск алгоритма в ширину
    visited = bfs([],graph0, strt1)

    #вывод
    final_output="Случайносгенерированный словарь смежности вершин:  <br>  " + str(graph0) + "<br><br> Матрица смежности вершин: <br>" + str(mtrx) + "<br><br> Порядок обхода: <br> " + str(visited) + "<br><br> Обход был начат в вершине: <br> " + str(strt1)+"<br><br> Имя сгенерированного графа: <br>" + str(gr) +""
    return(final_output)



