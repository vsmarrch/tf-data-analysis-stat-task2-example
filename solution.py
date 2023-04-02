import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 260376781 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    s_squared = np.var(x, ddof=1)
    disp_coef = 23 * (2 - np.pi / 2)
    
    nom = (n - 1) * s_squared
    rv = chi2(df = n - 1)
    left = rv.ppf(1 - alpha / 2) * disp_coef
    right = rv.ppf(alpha / 2) * disp_coef
    
    return np.sqrt(nom / left), np.sqrt(nom / right)
