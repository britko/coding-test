while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    a, b = min(a, b), max(a, b)
    b, c = min(b, c), max(b, c)

    print('right') if a**2 + b**2 == c**2 else print('wrong')