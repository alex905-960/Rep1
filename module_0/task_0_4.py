#!/usr/bin/env python
# coding: utf-8

# In[69]:


import numpy as np
def game_core_v4(number):
    '''Угадываем число с учетотм информации о том, больше загаданное число или меньше предполагаемого
    Функция принимает загаданное число и возвращает число попыток - методом нахождения середны диапазона'''
    cnt=0 #счетчик попыток
    low_limit=0 #нижняя граница поиска числа
    high_limit=101 #верхняя граница поиска числа
    predict=50 #предсказываемое число
    
    while 1==1: #бесконечный цикл
        cnt+=1 #приращение счетчика попыток
        if predict==number: #Если число угадано
            return cnt
        elif predict>number: #если число больше загаданного, коррекция границ
            high_limit=predict
            predict=int((low_limit+predict)/2)
        else: #если число меньше загаданного, коррекция границ
            low_limit=predict
            predict=int((high_limit+predict)/2)
            
def game_core_v3(number):
    '''Угадываем число с учетотм информации о том, больше загаданное число или меньше предполагаемого
    Функция принимает загаданное число и возвращает число попыток - методом random в указанном диапазоне'''
    cnt=0 #счетчик попыток
    low_limit=1 #нижняя граница поиска числа
    high_limit=100 #верхняя граница поиска числа
    
    while 1==1: #бесконечный цикл
        cnt+=1
        if low_limit>=(high_limit-1): #Если границы сузились до одного числа, то это и есть загаданное число
            return cnt
        predict=np.random.randint(low_limit,high_limit-1) # предполагаемое число
        if predict==number: #Если число угадано
            return cnt
        elif predict>number: #Если предполагаемое число больше загаднного
            high_limit=predict-1
        else: #Если предполагаемое число не больше и не равно загаданному, т.е. меньше
            low_limit=predict+1

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v4) #Проверка функции при логическом поиске загаданного числа
score_game(game_core_v3) #Проверка функции при логическо-рандомном поиске загаданного числа
 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




