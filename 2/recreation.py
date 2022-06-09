import math


def split_to_intervals(data: list):
    result = [[], [], []]

    n = len(data)

    lower = min(data)
    upper = max(data)

    dif = upper - lower

    k = int(1 + 3.322 * math.log(n, 2))
    h = dif / k

    current_bound = lower + h * 20
    k = 17
    for i in range(k):
        result[0].append(current_bound)
        current_bound += h
        result[1].append(current_bound)

        result[2].append(len([j for j in data if result[0][i] <= j <= result[1][i]]))

    return result


def split_to_discrete(data: list) -> dict:
    counts = {}

    for p in data:
        if p not in counts:
            counts[p] = 1
        else:
            counts[p] += 1

    return counts
