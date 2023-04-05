import pandas as pd
import numpy as np


chat_id = 557932710 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    import statistics as st
    
    y = [z - 270 for z in x]
    
    if(len(x) > 200):
        x1 = sum(np.log(y))/len(x)
    else:
        x1 = st.median(np.log(y))
    
    return x1 # Ваш ответ
