import matplotlib.pyplot as plt
from interval_estimates import *


def expon(a, b):
    return a * math.exp(-a*b)


# гистограмма
def create_bar_chart(inp_data: list) -> None:
    plt.style.use('_mpl-gallery')

    n = len(inp_data)

    n_data = []

    data = split_to_intervals(inp_data)
    data.append([((data[1][i] + data[0][i]) / 2) for i in range(len(data[0]))])

    mean = get_mean(inp_data)
    sq_dev = get_square_root_deviation(inp_data)
    p = mean / (sq_dev ** 2)
    lamb = 1 / mean

    n = sum(data[2])
    print(n)
    print(data[2])
    print(data[3])

    x = [(data[1][i] + data[0][i]) / 2 for i in range(len(data[0]))]
    # x = np.arange(-1, 3, 0.001)
    print(x)
    plt.figure(figsize=(10, 7))

    mean = 0.1244
    print(lamb)

    plt.hist(inp_data, 50, density=True)

    pdf = [expon(1/mean, i) for i in x]
    plt.plot(x, pdf, 'r-', lw=2, alpha=0.6, label='expon pdf', color='green')

    plt.show()
