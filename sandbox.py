def sum_eo(n , t):
    if t == "e":
        start = 2
        print(f'{n}')
    elif t == 'o':
        start = 1
        print(f'{n}')
    else:
        return -1

    return sum(range(start,n,2))


x = sum_eo(8,"o")
print(x)