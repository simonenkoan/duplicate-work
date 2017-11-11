import os
import psutil
import sys
import shutil





name = input("Введите ваше имя:")

print(name, ", добрый день.")


def answer_choose():
    print("Отлично. Выберите несколько вариантов")
    print("[1] - вывести список файлов ")
    print("[2] - вывести информацию о текущей директории ")
    print("[3] - вывести информацию о количестве CPU ")
    print("[4] - дублирование файлов в текущей дирректории")

answer = ""

while answer != "q":
    answer = input("Давайте выполним несколько операций? Y/N")
    if answer == 'Y':
        answer_choose()
        delo = int(input("Введите вариант:"))
        if delo == 1:
            print(os.listdir())
        elif delo == 2:
            print(os.getcwd())
        elif delo == 3:
            print(psutil.cpu_count())
        elif delo == 4:
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                newFileName = (file_list[i] + ".dupl")
                print(newFileName)
                # копирование
                if os.path.isfile(file_list[i]):
                    shutil.copy(file_list[i], newFileName)
                # i = i + 1
                i += 1
        else:
            print(psutil.cpu_count())
    elif answer == "N":
        print("Приходдите когда будете готовы поработать")
    else:
        print("Кажется вы не определились. Возвращайтесть снова..")



