import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 841977 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    stat, critical_values, significance_levels = anderson_ksamp([x, y])
    p_value = significance_levels[np.where(critical_values >= stat)[0][0]]
    if p_value <= alpha:
        return True
    else:
        return False
