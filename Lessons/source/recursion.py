#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return factorial_iterative(n)
    # return factorial_recursive(n)

def factorial_iterative(n):
    #naming is a bit tricky b/c 'product' is technically also a factor
    product_factor = 1 #by default, multiplying by 1.
    while n > 0:
        product_factor *= n # "x *= y" MEANS "x = y*x"
        n -= 1
    return product_factor

def factorial_recursive(n):
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()


# Classmates' work presented in class


# def jasmine_factorial_iterative(n):
#     factorial = 1
#     #2nd argument of RANGE is exclusive (not inclusive), tho the 1st is inclusive.
#     #That's why it goes from 1 to n+1 - because that 2nd argument is exclusive!
#     for i in range(1, n+1):
#         print(factorial)
#         factorial *= i
#     return factorial