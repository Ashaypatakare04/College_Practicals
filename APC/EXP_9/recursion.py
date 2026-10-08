def q29_binary_search(lst, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif target < lst[mid]:
        return q29_binary_search(lst, target, low, mid - 1)
    return q29_binary_search(lst, target, mid + 1, high)

def q30_decimal_binary(n):
    if n == 0:
        return ""
    return q30_decimal_binary(n // 2) + str(n % 2)

def q31_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return q31_palindrome(s[1:-1])

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print(q29_binary_search(data, 30, 0, len(data) - 1))

    print(q30_decimal_binary(10))

    print(q31_palindrome("madam"))
