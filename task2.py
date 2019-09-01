def get_mean_value(arr):
    return sum(arr) / len(arr)

def load(filename):
    items = []
    data = open(filename)
    for line in data.readlines():
        x, y = map(float, line.strip().split())
        items.append([x, y])
    return items

def get_partitions(items):
    result = []
    for i in range(len(items) - 1):
        cur_el = items[i][0]
        next_el = items[i + 1][0]
        result.append((cur_el + next_el) / 2)
    return result


def getABValues(m, items):
    left = []
    right = []
    for i in range(len(items)):
        el = items[i][0]
        if el > m:
            right.append(el)
        else:
            left.append(el)

    return left, right

def f(a, b, m, x):
    if x > m:
        return b
    else:
        return a 


def get_min_index(arr):
    min_value = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] < min_value:
            index = i
            min_value = arr[i]
    return index

def get_result_varients(partitions):
    result_variants = []
    for m in partitions:
        left, right = getABValues(m, items)
        meanLeft = get_mean_value(left)
        meanRight = get_mean_value(right)
        result_variants.append((meanLeft, meanRight, m))
    return result_variants

def get_sse_values(result_variants, items):
    sse_values = []
    for i in range(len(result_variants)):
        a, b, m = result_variants[i]
        sse = 0

        for i in range(len(items)):
            el = items[i]
            q = f(a, b, m, el[0]) - el[1]
            sse += q * q

        sse_values.append(sse)
    return sse_values

def get_result(sse_values, result_variants):
    result_index = get_min_index(sse_values)
    best_a, best_b, best_m = result_variants[result_index]
    result = str(best_a) + ' ' + str(best_b) + ' ' + str(best_m)
    return result

def save(filename, result):
    output_file = open(filename, 'w')
    output_file.write(result)
    output_file.close()

items = load('stump.in')
items.sort()
partitions = get_partitions(items)
result_variants = get_result_varients(partitions)
sse_values = get_sse_values(result_variants, items)
result = get_result(sse_values, result_variants)
save('stump.out', result)