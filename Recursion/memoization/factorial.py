# using recursion
def factorial(n):
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


# using memoization
def factorial1(n,d):
    if n in d:
        return d[n]
    if n<1:
        return 1
    d[n]=n * factorial1(n-1,d)
    return d[n]
d ={1:1}
print(factorial1(5,d))
