# 1.	Дан список. Выведите те его элементы, которые встречаются в списке только один раз.

# a = [1,6,'h', 8, 1, 9, 'h','m']
# b = []
# for i in a:
#     if a.count(i) == 1: b.append(i)
# print(*b)

#2. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

# a = [1,1,1,1,1,1,1,1,2,2]
# 1 1 1 1 1 1 1 1
# 0 1 2 3 4 5 6 7
# 01, 02, 03, 04, 05, 06, 07
# 12, 13,14,15,16,17
# 23, 24,25,26,27
# 34,35,36,37
# 45,46,47
# 56,57
# 67
# count1 = 0
# count2 = 0
# b = set(a)
# for i in b:
#     count1 += a.count(i)
#     for j in range(1,count1):
#         count2 += j
#     count1 = 0
# print(count2)

#3. 3.	Даны два кортежа:
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1)	Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран (Сумма больше в кортеже - ..)
# 2)	Вывести на экран порядковые номера минимальных и максимальных элементов этих кортежей (index).
# if sum(C_1)> sum(C_2): print('C_1 больше')
# elif sum(C_2)> sum(C_1): print('C_2 больше')
# else: print('Суммы равны')
# print(C_1.index(max(C_1))+1)
# print(C_2.index(max(C_2))+1)

#4.
# a = ('An apple a day keeps the doctor away'.lower()).split()
# a = ''.join(a)
# d = {i: a.count(i) for i in a}
# print(d)

#5. Даны два списка чисел.
# Посчитайте, сколько чисел содержится одновременно как в первом списке,
# так и во втором.
# C_1 = [35, 78,21,37, 2,98, 6, 100, 231]
# C_2 = [45, 21,124,76,5,23,91,234]
#
# count = 0
#
# for i in C_1:
#     if i in C_2: count+=1
# print(count)
# print(len(set(C_1)&set(C_2)))

#6. 6.	В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу
# av = 0
#
# with open('puples.txt', encoding='utf-8') as f:
#     uch = f.readlines()
# for i in uch:
#     a = i.strip()
#     if int(a[-1])<3: print(a)
#     av += int(a[-1])
# print(round(av/len(uch),1))
# print('%.2f' % (av/len(uch)))

# GIT - система контроля версий вашего проекта в Python
# git push - запушить какие-либо изменения (сохранить инофрмацию об этом)
#Github - сайт, куда будем загружать код и информацию о коде
#Bitbucket, GitLab - аналогичные платформы

#commit - чек-пойнт, или точка сохранения изменений, или информация об изменении

# git имеет 4 состояния:
#1. untracked (неотслеживаемое)
#2.modified (измененное)
#3. staged (подготовленное)
#4. committed (закомичен)

# Коммит - объект для управления контроля версий. Он содержит все изменения зя время коммита.
# Все коммиты связаны между собой и имеют односвязный список.

# У каждого коммита есть своя информация - метаданные:
#1. Уникальный номер (id) коммита, по которому можно к нему перейти
#2. Информация об авторе коммита - его имя
#3. Дата создания коммита
#4. Комментарий, который описывает, что было сделано во время этого коммита

#Ветка - это указатель какого-то коммита

#При работе с гитом:
# Не делать коммит после каждого изменения, а только в случаях:
#1. Создан новый функционал
#2. Добавлен блок кода
#3. Исправлена ошибка в коде
#4. Сохранить код в конце рабочего дня

# Программы для работы с github:
# GitHub desctop
# Sourcetree
# GitKraken

