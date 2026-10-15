def win_sum(n):
    arr = [0] * n + [1] * n
    for i in range(len(arr) - n + 1):
        window = arr[i:i+n]
        if sum(window) == n:
            return i
    return -1

n = int(input("Enter n:"))

print("Array:", [0] * n + [1] * n)
print("Starting index:", win_sum(n))