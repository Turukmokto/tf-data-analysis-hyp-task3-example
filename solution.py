import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu


chat_id = 1112700607  # Ваш chat ID, не меняйте название переменной


def solution(ar1: np.array, ar2: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    cnst = 0.07
    return mannwhitneyu(ar1, ar2, alternative="less").pvalue < cnst
