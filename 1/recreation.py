def split_to_intervals(data: list):
    result = [[], [], []]

    n = len(data)

    lower = min(data)
    upper = max(data)

    dif = upper - lower

    k = 25
    h = 1

    current_bound = lower
    for i in range(k):
        result[0].append(current_bound)
        result[1].append(current_bound)
        current_bound += h

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
