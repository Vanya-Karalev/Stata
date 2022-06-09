import math
import matplotlib.pyplot as plt
from point_estimators import *


def pois(a, b):
    return ((a ** b) / math.gamma(b + 1)) * math.exp(-a)


def geom(p, k):
    return ((1 - p) ** k) * p


def expon(a, b):
    return a * math.exp(-a*b)


# гистограмма
def create_bar_chart(inp_data: list) -> None:
    plt.style.use('_mpl-gallery')

    n = len(inp_data)

    data = split_to_intervals(inp_data)
    data.append([((data[1][i] + data[0][i]) / 2) for i in range(len(data[0]))])

    mean = get_mean(inp_data)
    sq_dev = get_square_root_deviation(inp_data)
    p = mean / (sq_dev ** 2)
    p = 0.297
    l = 1 / mean

    print(data[2])

    x = [(data[1][i] + data[0][i]) / 2 for i in range(len(data[0]))]
    x = np.arange(0, 20)
    y = np.array([(i + 1) / 1e5 for i in data[2]])

    plt.figure(figsize=(10,7))

    mean = np.mean(inp_data)
    print(mean)

    plt.hist(inp_data, 70)
    x = np.arange(0, 20, 1)

    # Visualizing the results
    pdf = [geom(p, i-1) * n for i in x]
    plt.plot(x, pdf, 'r-', lw=2, alpha=0.6, label='expon pdf')

    check = [data[2][i] / data[2][i-1] if data[2][i-1] > 0 else 1e9 for i in range(1, len(data[2]))]
    print(check)

    plt.show()
