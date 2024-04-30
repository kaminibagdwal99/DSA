# using REcursion


def fibo(number):
    if number ==0 or number ==1:
        return 1
    if number >=2:
        return fibo(number-1) + fibo(number-2)

print(fibo(5))


# using memoization
def fibo(number,d):
    if number in d:
        return d[number]
    if number <=2:
        return 1
    d[number] =fibo(number-1,d) + fibo(number-2,d)
    return d[number]
d = {0:1,1:1}
print(fibo(6,d))