# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:03:25 2021

@author: ИнтелАв
"""
# Задание 1

out_f = open("out_file.txt", "w")
Out_str = "1"
while Out_str != "":
    Out_str = input("Введите строку (для выхода введите пустую строку):")
    out_f.write(Out_str + "\n")
out_f.close()

# задание 2

my_f = open("out_file.txt", "r")
lines2 = my_f.readlines()
KolStrok = len(lines2)
KolSlov = 0
for i in range(0,len(lines2)):
    KolSlov += len(lines2[i].split(" "))

# задание 3
my_f3 = open("oklad.txt", "r", encoding="utf-8")
lines3 = my_f3.readlines()
SredOklad = 0
for i in range(0,len(lines3)):
    list3 = lines3[i].strip().split("-")
    SredOklad += int(list3[1])
    if int(list3[1]) < 20000:
        print(list3[0])
SredOklad = SredOklad/len(lines3)

# задание 4
my_f4 = open("chislaEng.txt", "r", encoding="utf-8")
out_f4 = open("chislaRus.txt", "w", encoding="utf-8")
for line in my_f4:
     out_f4.write(line.replace("One", "Один").replace("Two", "Два").replace("Three", "Три").replace("Four", "Четыре"))
out_f4.close()


# задание 5
out_f5= open("Chisla5.txt", "w", encoding="utf-8")
Out_str = "1"
while Out_str != "":
    Out_str = input("Введите число (для выхода введите пустую строку):")
    out_f5.write(Out_str + " ")
out_f5.close()
 
#   используется в задании 5 и 6
def InCount5(List5): 
    str_list5 = List5.split(" ")
    n5 = 0
    for i in str_list5:        
        try:
           n5 += int(i)
        except:
            pass
    return n5

my_f5 = open("Chisla5.txt", "r", encoding="utf-8")
n5 = InCount5(my_f5.readline())


# задание 6
my_f6 = open("slovar.txt", "r", encoding="utf-8")
Dict6 = {}
for st in my_f6.readlines():
    list6 = st.strip().split(":")
    Dict6[list6[0]] = InCount5(''.join([i for i in list6[1] if i.isdigit() or i == " "]))

# задание 7
import json
with open("firms.txt") as f_obj7:
    Dict7 = {}
    kolPribyl = 0
    SrPribl = 0
    for line in f_obj7:
        list7 = line.split(" ")
        if int(list7[2])-int(list7[3])>0:
            SrPribl += int(list7[2])-int(list7[3])
            kolPribyl += 1
        Dict7[list7[0]] = int(list7[2])-int(list7[3])
    
    SrPribl = SrPribl/kolPribyl
    list7 = [Dict7, {"average_profit": SrPribl}]
    with open("my_file7.json", "w") as write_f:
        json.dump(list7, write_f)
    

    




