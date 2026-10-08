def q9_largest(lst):
    large = lst[0]
    for x in lst:
        if x > large:
            large = x
    return large

def q13_average(lst):
    return sum(lst) / len(lst)

def q14_count_element(lst, element):
    count = 0
    for x in lst:
        if x == element:
            count += 1
    return count

def q15_unique(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

def q16_second_largest(lst):
    values = list(set(lst))
    values.sort()
    return values[-2]

def q22_statistics(lst):
    total = sum(lst)
    return min(lst), max(lst), total, total / len(lst)

if __name__ == "__main__":
    data = [10, 20, 20, 30, 40, 50]
    print(q9_largest(data))
    print(q13_average(data))
    print(q14_count_element(data, 20))
    print(q15_unique(data))
    print(q16_second_largest(data))
    print(q22_statistics(data))
