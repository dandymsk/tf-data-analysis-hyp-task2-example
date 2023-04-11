import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 841977 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    stat, p = ks_2samp(x, y)
    if p <= alpha:
        return True
    else:
        return False
