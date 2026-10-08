def largest(lst):
    large = lst[0]
    for x in lst:
        if x > large:
            large = x
    return large

def average(lst):
    return sum(lst) / len(lst)

def count_element(lst, element):
    count = 0
    for x in lst:
        if x == element:
            count += 1
    return count

def unique(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

def second_largest(lst):
    values = list(set(lst))
    values.sort()
    return values[-2]

def statistics(lst):
    total = sum(lst)
    return min(lst), max(lst), total, total / len(lst)

data = [10, 20, 20, 30, 40, 50]

print("Largest Element:", largest(data))
print("Average:", average(data))
print("Element Count:", count_element(data, 20))
print("Unique Elements:", unique(data))
print("Second Largest:", second_largest(data))
print("Statistics:", statistics(data))
