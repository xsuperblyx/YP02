"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        matrixtext='Случайносгенерированный граф в виде матрицы: ',
        grphtitle='Онлайн калькулятор по ориентированным и неориентированным графам',
        title='Главная',
        graphopr='При помощи данного калькулятора вы сможете: 1) Найти остовное дерево графа с помощью алогиртма поиска "в ширину"; 2) Найти остовное дерево графа с помощью алгоритма поиска "в глубину"; 3) Найти кратчайший остов графа с помощью алгоритма Краскала',
        vr1='Метод "в ширину"',
        vr2='Метод "в глубину"',
        vr3='Метод Крускала',
        vib='Выберите метод',
        matrx='Случайносгенерированный словарь смежности вершин',
        gen='Генерировать'
    )


@route('/var3')
@view('var3')
def contact():
    """Renders the contact page."""
    return dict(
        title='Главная',
        message='Поиск кратчайшего остова графа с помощью алгоритма Краскала',
        vr1='Метод "в ширину"',
        vr2='Метод "в глубину"',
        vr3='Метод Крускала',
        zapvar3='Запуск'
    )

@route('/var2')
@view('var2')
def about():
    """Renders the about page."""
    return dict(
        title='Главная',
        message='Поиск остовного дерева графа с помощью алгоритма "в глубину"',
        vr1='Метод "в ширину"',
        vr2='Метод "в глубину"',
        vr3='Метод Крускала',
        zapvar2='Запуск'
    )
@route ('/var1')
@view ('var1')
def var1():
    return dict(
        title='Главная',
        message='Поиск остовного дерева графа с помощью алгоритма "в ширину"',
        vr1='Метод "в ширину"',
        vr2='Метод "в глубину"',
        vr3='Метод Крускала',
        zapvar1='Запуск'
        )
