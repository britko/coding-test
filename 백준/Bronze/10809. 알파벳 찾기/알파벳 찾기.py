s = input()
arr = [-1 for _ in range(26)]

for i in range(len(s)):
    idx = ord(s[i]) - 97
    if arr[idx] == -1:
        arr[idx] = i

for i in range(len(arr)):
    print(arr[i], end=' ')
