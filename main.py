

try:
    print("Загрузка sympy...")
    import sympy
except:
    print("Ошибка при загрузке модуля sympy.\nПроверте то, что вы установили sympy")
    exit(1)
print("Загрузка других модулей...")

from string import ascii_letters as let
import config as cfg
from settings import *


def main():
    selected_item = -1
    selected_item2 = -1
    while True:
        cfg.clr()

        if selected_item == -1:
            print(cfg.TEXT)
            print("Главное меню")
            print(cfg.SELECT)
            try:
                selected_item = int(input(">>> "))
            except:
                continue

        elif selected_item == 1:  # Если выбрали Решение уравнений
            while True:
                cfg.clr()
                if selected_item2 == -1: # Начальный текст
                    print(cfg.TEXT)
                    print("Решение уравнений")
                    print(cfg.SELECT2)
                    try:
                        selected_item2 = int(input(">>> "))
                    except:
                        continue
                elif selected_item2 == 1:  # Задать символ
                    cfg.clr()
                    print(cfg.GUIDE)
                    input("Нажмите [ENTER] чтобы вернуться назад")
                    selected_item2 = -1
                elif selected_item2 == 2:
                    cfg.clr()
                    print(cfg.TEXT)
                    print("Напишите уравнение")
                    yr = input(">>> ").strip().replace(" ", "").split("=")
                    if len(yr) != 2:
                        print("Неверное уравнение")
                        input("Нажмите [ENTER] чтобы вернуться назад")
                        selected_item2 = -1
                    else:
                        try:
                            # DEBUG: print(f"{yr=}; {x=}")
                            answer = sympy.solve(sympy.Eq(eval(yr[0]), eval(yr[1])))
                        except:
                            print("Неверное уравнение")
                            input("Нажмите [ENTER] чтобы вернуться назад")
                            selected_item2 = -1
                        else:
                            print("Ответ(ы): {}".format(", ".join(str(v) for v in answer)))
                            input("Нажмите [ENTER] чтобы вернуться назад")
                            selected_item2 = -1
                elif selected_item2 == 3:  # Назад
                    break
            selected_item = -1
            selected_item2 = -1
        elif selected_item == 2:  # Если выбрали Инфо
            print(cfg.CREDITS)
            input("Нажмите [ENTER] чтобы вернуться назад")
            selected_item = -1
        elif selected_item == 3:  # Если выбрали Выход
            selected_item = -1
            cfg.clr()
            exit(0)


if __name__ == '__main__':
    for sym in symbols:
        if not (str(sym) in list(let)):
            print(f"При загрузке найден неверный символ в настройках")
            exit(1)
    main()
