import os
import psutil
import shutil

name = input("Введите ваше имя:")

print(name, ", добрый день.")

def answer_choose():
    print("")
    print("Отлично. Выберите операцию")
    print("[1] - вывести список файлов ")
    print("[2] - вывести информацию о текущей директории ")
    print("[3] - вывести информацию о количестве CPU ")
    print("[4] - дублирование файлов в текущей дирректории")
    print("[0] - для выхода в меню")
    print("")

def proverka_file(filename_i):
    if os.path.isfile(filename_i):
        shutil.copy(filename_i, newFileName)
    # i = i + 1

answer = ""

while answer != "q":
    answer = input("Давайте выполним несколько операций? Y/N")
    if answer == 'Y':
        answer_choose()
        delo = ""
        while delo != 0:
            delo = int(input("Введите вариант:"))
            print("")
            if delo == 1:
                print("Результат:")
                print(os.listdir())
                answer_choose()
            elif delo == 2:
                print("Результат:")
                print(os.getcwd())
                answer_choose()
            elif delo == 3:
                print("Результат:")
                print(psutil.cpu_count())
                answer_choose()
            elif delo == 4:
                print("Результат:")
                file_list = os.listdir()
                i = 0
                while i < len(file_list):
                    newFileName = (file_list[i] + ".dupl")
                    print(newFileName)
                    # копирование
                    proverka_file(file_list[i])
                    i += 1
                answer_choose()
            else:
                pass

    elif answer == "N":
        print("Приходдите когда будете готовы поработать")
    else:
        print("Кажется вы не определились. Возвращайтесть снова..")

print(" Всего вам доброго")



