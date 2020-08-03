def factorize(x):
    '''
    The function returns a list of numbers that are divisors of the number x
    x - int positive number
    >>> factorize(555)
    [3, 5, 37]
    >>> factorize(12345)
    [3, 5, 823]
    '''
    divisors = set()
    divisor = 2
    while x >= divisor ** 0.5:
        if x % divisor == 0:
            divisors.add(divisor)
            x //= divisor
        else:
            divisor += 1
    return sorted(divisors)

def main():
    import doctest
    doctest.testmod()
    print(factorize(int(input())))

if __name__ == '__main__':
    main()
