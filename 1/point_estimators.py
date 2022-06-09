import numpy as np
import scipy.stats
from recreation import *


# медиана
def get_median(data: list) -> float:
    a = np.sort(data)
    return a[int(len(a) / 2)]


# мода
def get_discrete_moda(data: list) -> float:
    counts = split_to_discrete(data)

    # Проходимся по словарю и ищем максимальное количество повторений
    maxp = 0
    mode_price = None
    for k, v in counts.items():
        if maxp < v:
            maxp = v
            mode_price = k

    return mode_price


def get_interval_moda(inp_data) -> float:

    data = split_to_intervals(inp_data)

    max_n = 0
    mode_i = None
    for i in range(len(data[0])):
        if max_n < data[2][i]:
            max_n = data[2][i]
            mode_i = i

    h = data[1][mode_i] - data[0][mode_i]

    n_m_sub_1 = 0
    n_m_add_1 = 0

    if mode_i - 1 >= 0:
        n_m_sub_1 = data[2][mode_i] - data[2][mode_i - 1]
    else:
        n_m_sub_1 = data[2][mode_i]

    if mode_i + 1 < len(data[0]):
        n_m_add_1 = data[2][mode_i] - data[2][mode_i + 1]
    else:
        n_m_add_1 = data[2][mode_i]

    result = data[0][mode_i] + ((n_m_sub_1 / (n_m_sub_1 + n_m_add_1)) * h)

    return result


# среднее значение
def get_mean(data: list) -> float:
    result = sum(data) / len(data)
    return result


# корень дисперсии
def get_square_root_deviation(data: list) -> float:
    diffs = 0
    avg = sum(data) / len(data)
    for n in data:
        diffs += (n - avg) ** 2
    return (diffs / (len(data) - 1)) ** 0.5


# доверит интервал для ср знач
def get_mean_intervals(data: list, gamma=0.99) -> None:
    mean = get_mean(data)
    sq_dev = get_square_root_deviation(data)
    n = len(data)

    t = scipy.stats.t.ppf(gamma, n - 1)
    delta = t * sq_dev / np.sqrt(n)

    mean_left = mean - delta
    mean_right = mean + delta

    print(f'{mean_left} < mean_value < {mean_right}')


# доверит интервал для сред кв знач
def get_sq_dev_intervals(data: list, gamma=0.99) -> None:
    mean = get_mean(data)
    sq_dev = get_square_root_deviation(data)
    n = len(data)

    a1 = (1 - gamma) / 2.0
    a2 = (1 + gamma) / 2.0

    sq_dev_left = np.sqrt((n - 1) / scipy.stats.chi2.ppf(a2, n - 1)) * sq_dev
    sq_dev_right = np.sqrt((n - 1) / scipy.stats.chi2.ppf(a1, n - 1)) * sq_dev

    print(f'{sq_dev_left : .4f} < square_root_deviation < {sq_dev_right : .4f}')


def z_test(data: list, gamma=0.99) -> float:
    mean = get_mean(data)
    sq_dev = get_square_root_deviation(data)
    n = len(data)

    t = scipy.stats.t.ppf(gamma, n - 1)
    delta = t * sq_dev / np.sqrt(n)

    mean_left = mean - delta
    mean_right = mean + delta

    return scipy.stats.norm.cdf((mean_right - mean) / sq_dev * np.sqrt(n))


def t_test(data: list, gamma=0.99) -> float:
    mean = get_mean(data)
    sq_dev = get_square_root_deviation(data)
    n = len(data)

    t = scipy.stats.t.ppf(gamma, n - 1)
    delta = t * sq_dev / np.sqrt(n)

    mean_left = mean - delta
    mean_right = mean + delta

    return scipy.stats.t.cdf((mean_right - mean) / sq_dev * np.sqrt(n), df=n - 1)


def f_test(data: list, gamma=0.99):
    mean = get_mean(data)
    sq_dev = get_square_root_deviation(data)
    n = len(data)

    a1 = (1 - gamma) / 2.0
    a2 = (1 + gamma) / 2.0

    sq_dev_left = np.sqrt((n - 1) / scipy.stats.chi2.ppf(a2, n - 1)) * sq_dev
    sq_dev_right = np.sqrt((n - 1) / scipy.stats.chi2.ppf(a1, n - 1)) * sq_dev

    return scipy.stats.f.cdf((sq_dev_right ** 2) / (sq_dev_left ** 2), n - 1, n - 1)
