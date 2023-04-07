import pandas as pd
import numpy as np

from scipy.stats import chi2

chat_id = 260376781 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    
    x2 = [xi**2 for xi in x]
    x2_sum = sum(x2)
    
    chi2_rv = chi2(df=2 * n)
    
    left = chi2_rv.ppf(1 - alpha / 2) #b
    right = chi2_rv.ppf(alpha / 2) #a
    
    return np.sqrt(x2_sum / (left * 23)), np.sqrt(x2_sum / (right * 23))
