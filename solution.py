import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
import math
chat_id = 628156322 # Ваш chat ID, не меняйте название переменной
def solution(sales_control : int, requests_control: int, sales_test: int, requests_test: int) -> bool:
    p1 = sales_control / requests_control
    p2 = sales_test / requests_test
    p = (sales_control + sales_test) / (requests_control + requests_test)
    n1 = requests_control
    n2 = requests_test
    z_alpha = abs(round(norm.ppf(0.08), 2))

    z = (p1 - p2) / math.sqrt(p * (1 - p) * (1/n1 + 1/n2))

    return z < -z_alpha
