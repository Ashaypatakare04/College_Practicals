def binary_search(lst, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif target < lst[mid]:
        return binary_search(lst, target, low, mid - 1)
    return binary_search(lst, target, mid + 1, high)

def decimal_binary(n):
    if n == 0:
        return ""
    return decimal_binary(n // 2) + str(n % 2)

def recursive_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return recursive_palindrome(s[1:-1])

data = [10, 20, 30, 40, 50]

print("Binary Search Index:", binary_search(data, 30, 0, len(data) - 1))
print("Decimal to Binary:", decimal_binary(10))
print("Recursive Palindrome:", recursive_palindrome("madam"))
