import math
from point_estimators import *
from scipy.stats import chi2
import scipy.special


def debug(data, theoretical_frequencies, pois_values, n, k, gen_val):
    print('-' * 50)
    print(f'Mean value      : {gen_val}')
    print(f'Sun Ni          : {n}')
    print(f'k               : {k}')
    print(f'sum             : {sum(theoretical_frequencies)}')
    print(f'need sum        : {sum(data[2])}')

    print(data[2])

    print('\n\npois_values')
    print(pois_values)

    print('\n\ntheoretical_frequencies')
    print(theoretical_frequencies)


def pois(a, b):
    return ((a ** b) / math.gamma(b + 1)) * math.exp(-a)


def poisson_check(inp_data: list, meaning_level: float = 0.01):

    data = split_to_intervals(inp_data)

    n = sum(data[2])
    k = len(data[0]) - 2
    chi2_critical = chi2.ppf(meaning_level, k)

    poisson_lambda = get_mean(inp_data)

    x = [(data[1][i] + data[0][i]) / 2 for i in range(len(data[0]))]

    pois_values = [pois(poisson_lambda, x[i]) for i in range(len(data[0]))]
    theoretical_frequencies = [i * n for i in pois_values]

    chi2_observ = sum([((data[2][i] - theoretical_frequencies[i]) ** 2) / theoretical_frequencies[i] for i in range(len(data[0]))])

    print(f'chi2 critical   : {chi2_critical}')
    print(f'chi2 observable : {chi2_observ} \n')

    if chi2_observ < chi2_critical:
        print(f"На уровне значимости  {meaning_level} нет оснований отвергать гипотезу  о том, что генеральная "
              f"совокупность распределена по Пуассону")

    else:
        print(f'На уровне значимости  {meaning_level} отвергаем гипотезу о распределении совокупности согласно '
              f'распределению Пуассона')

    print('-' * 50)


def expon(a, b):
    return a * math.exp(-a*b)


def exponential_check(inp_data: list, meaning_level: float = 0.01):

    data = split_to_intervals(inp_data)

    n = sum(data[2])
    k = len(data[0]) - 2
    chi2_critical = chi2.ppf(meaning_level, k)

    x = [(data[1][i] + data[0][i]) / 2 for i in range(len(data[0]))]

    # 0.2906317753532629
    mean = sum([x[i] * data[2][i] for i in range(len(data[2]))]) / n
    exponential_lambda = 1 / mean

    exp_values = [expon(exponential_lambda, x[i]) for i in range(len(data[0]))]
    theoretical_frequencies = [i * n for i in exp_values]

    chi2_observ = sum([((data[2][i] - theoretical_frequencies[i]) ** 2) / theoretical_frequencies[i] for i in range(len(data[0]))])

    debug(data, theoretical_frequencies, exp_values, n, k, mean)

    print(f'chi2 critical   : {chi2_critical}')
    print(f'chi2 observable : {chi2_observ} \n')

    if chi2_observ < chi2_critical:
        print(f"На уровне значимости  {meaning_level} нет оснований отвергать гипотезу  о том, что генеральная "
              f"совокупность распределена эекспоненциально")

    else:
        print(f'На уровне значимости  {meaning_level} отвергаем гипотезу о распределении совокупности согласно '
              f'эекспоненциальному распределению')

    print('-' * 50)


def norm(a, b, c):
    return 1.0 / (b * np.sqrt(2 * np.pi)) * np.exp(-(c - a) ** 2 / (2 * b ** 2))


def normal_check(inp_data: list, meaning_level: float = 0.01):

    data = split_to_intervals(inp_data)

    n = sum(data[2])
    k = len(data[0]) - 2
    chi2_critical = chi2.ppf(meaning_level, k)

    mean = get_mean(inp_data)
    sq_dev = get_square_root_deviation(inp_data)

    x = [(data[1][i] + data[0][i]) / 2 for i in range(len(data[0]))]

    norm_values = [norm(mean, sq_dev, x[i]) for i in range(len(data[0]))]
    theoretical_frequencies = [i * n for i in norm_values]

    chi2_observ = sum([((data[2][i] - theoretical_frequencies[i]) ** 2) / theoretical_frequencies[i] for i in range(len(data[0]))])

    print(f'chi2 critical   : {chi2_critical}')
    print(f'chi2 observable : {chi2_observ} \n')

    if chi2_observ < chi2_critical:
        print(f"На уровне значимости  {meaning_level} нет оснований отвергать гипотезу  о том, что генеральная "
              f"совокупность распределена нормально")

    else:
        print(f'На уровне значимости  {meaning_level} отвергаем гипотезу о распределении совокупности согласно '
              f' нормальному распределению')

    print('-' * 50)


def plain(a, b):
    return 1.0 / (b - a)


def plain_check(inp_data: list, meaning_level: float = 0.1):

    data = split_to_intervals(inp_data)
    # data[2] = [math.sqrt(i) for i in data[2]]

    mean = get_mean(inp_data)
    sq_dev = get_square_root_deviation(inp_data)
    b = mean + np.sqrt(3) * sq_dev
    a = 2 * mean - b

    n = sum(data[2])
    k = len(data[0]) - 2
    chi2_critical = chi2.ppf(meaning_level, k)

    x = [(data[1][i] + data[0][i]) / 2 for i in range(len(data[0]))]

    plain_values = [1.0 / (b - a) for i in range(len(data[0]))]
    theoretical_frequencies = [i * n for i in plain_values]

    chi2_observ = sum([((data[2][i] - theoretical_frequencies[i]) ** 2) / theoretical_frequencies[i] for i in range(len(data[0]))])

    print(f'chi2 critical   : {chi2_critical}')
    print(f'chi2 observable : {chi2_observ} \n')

    if chi2_observ < chi2_critical:
        print(f"На уровне значимости  {meaning_level} нет оснований отвергать гипотезу  о том, что генеральная "
              f"совокупность распределена равномерно")

    else:
        print(f'На уровне значимости  {meaning_level} отвергаем гипотезу о распределении совокупности согласно '
              f'равномерному распределению')

    print('-' * 50)


def bino(n, p, k):
    return scipy.special.comb(n, k, exact=True) * (p ** k) * ((1 - p) ** (n - k))


# ?????????????????????????????????????????
def binomoial_check(inp_data: list, meaning_level: float = 0.1):

    data = split_to_intervals(inp_data)

    n = sum(data[2])
    k = len(data[0]) - 2
    chi2_critical = chi2.ppf(meaning_level, k)

    p = get_mean(inp_data) / len(data[2])

    x = [(data[1][i] + data[0][i]) / 2 for i in range(len(data[0]))]

    pois_values = [bino(n, p, x[i]) for i in range(len(data[0]))]
    theoretical_frequencies = [i * n for i in pois_values]

    chi2_observ = sum([((data[2][i] - theoretical_frequencies[i]) ** 2) / (theoretical_frequencies[i] + 1e-30) for i in range(len(data[0]))])

    print(f'chi2 critical   : {chi2_critical}')
    print(f'chi2 observable : {chi2_observ} \n')

    if chi2_observ < chi2_critical:
        print(f"На уровне значимости  {meaning_level} нет оснований отвергать гипотезу  о том, что генеральная "
              f"совокупность распределена биномиально")

    else:
        print(f'На уровне значимости  {meaning_level} отвергаем гипотезу о распределении совокупности согласно '
              f'биномиальному распределению')

    print('-' * 50)


def geom(p, k):
    return ((1 - p) ** k) * p


def geometrik_check(inp_data: list, meaning_level: float = 0.1):
    data = split_to_intervals(inp_data)

    n = sum(data[2])
    k = len(data[0]) - 2
    chi2_critical = chi2.ppf(meaning_level, k)

    x = [(data[1][i] + data[0][i]) / 2 for i in range(len(data[0]))]

    # 0.2906317753532629
    mean = sum([x[i] * data[2][i] for i in range(len(data[2]))]) / n

    sq_dev = get_square_root_deviation(inp_data)

    p = mean / (sq_dev ** 2)

    print(p)

    p = 0.297

    plain_values = [geom(p, x[i] - 1) for i in range(len(data[0]))]
    theoretical_frequencies = [i * n for i in plain_values]

    chi2_observ = sum([((data[2][i] - theoretical_frequencies[i]) ** 2) / theoretical_frequencies[i] for i in
                       range(len(data[0]))])

    debug(data, theoretical_frequencies, plain_values, n, k, sq_dev)

    print(f'chi2 critical   : {chi2_critical}')
    print(f'chi2 observable : {chi2_observ} \n')

    if chi2_observ < chi2_critical:
        print(f"На уровне значимости  {meaning_level} нет оснований отвергать гипотезу  о том, что генеральная "
              f"совокупность распределена геометрически")

    else:
        print(f'На уровне значимости  {meaning_level} отвергаем гипотезу о распределении совокупности согласно '
              f'геометрическому распределению')

    print('-' * 50)