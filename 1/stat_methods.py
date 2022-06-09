from charts_module import create_bar_chart
from interval_estimates import *


def complex_explore(data: list) -> None:

    create_bar_chart(data)

    # point estimators
    print('-' * 50)
    print(f'Mean value            : {get_mean(data)}')
    print(f'Median value          : {get_median(data)}')
    print(f'Mode for discrete     : {get_discrete_moda(data)}')
    print(f'Moda for intervals    : {get_interval_moda(data)}')
    print(f'Square root deviation : {get_square_root_deviation(data)}')
    print(f'Dispersion value      : {get_square_root_deviation(data) ** 2}')
    print('-' * 50)

    # interval estimators
    print('-' * 50)
    print(f'Trust intervals : ')
    print(f'       {get_mean_intervals(data)}')
    print(f'       {get_sq_dev_intervals(data)}')
    print('-' * 50)

    # special values
    print('-' * 50)
    print(f't-value               : {t_test(data)}')
    print(f'z-value               : {z_test(data)}')
    print(f'f-value               : {f_test(data)}')
    print('-' * 50)

    # distribution check
    geometrik_check(data)
