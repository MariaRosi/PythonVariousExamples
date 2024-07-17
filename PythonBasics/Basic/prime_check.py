for n in range(2, 10):
    for i in range(2, n):
        if n % i == 0:
            print(f'{n} is not a prime number {i} * {n//i}' )
            break
    else:
        print(f'{n} is a prime number')