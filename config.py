from os import system, name

TEXT = """
███╗   ███╗ █████╗ ████████╗██╗  ██╗      ██╗
████╗ ████║██╔══██╗╚══██╔══╝██║  ██║      ██║
██╔████╔██║███████║   ██║   ███████║ ████████████╗
██║╚██╔╝██║██╔══██║   ██║   ██╔══██║      ██╔════╝
██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║      ██║
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝      ╚═╝
"""

SELECT = """Пункты выбора:
1: Решение уравнений
2: Инфо
3: Выход
"""

SELECT2 = """Пункты выбора:
1: Задать символ
2: Решить уравнение
3: Назад
"""
GUIDE = """Чтобы задать символ нужно:
* Открыть файл settings.py
* Найти графу symbols = (...)
* Добавить через запятую символы, например:
    x = Symbol("x"), 
    y = Symbol("y") # Новый символ 
    symbols = [x, y]
* Объяснения:
  y = Symbol("y")
  ^           ^
  Новый символ|     
              Новый символ
  symbols = [x, y]
                ^
                Новый символ 
  Заметка: Символы, где помечены (новые) должны быть ОДИНАКОВЫМИ и надо добавить их в symbols!
"""

CREDITS = """Инфо
* Сделал на Python
* Использовал библиотеку sympy
* Если понравилась моя работа, то поставте звезду на репозитории :3
"""
def clr():
    system('cls' if name == 'nt' else 'clear')
