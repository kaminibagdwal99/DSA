
def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
    return matrix


def setZeroes(matrix):
    pair=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                pair.append([i,j])
    for r,c in pair:
        for i in range(len(matrix)):
            matrix[i][c]=0
        for  i in range(len(matrix[0])):
            matrix[r][i]=0
    return matrix

def isHappy(n):
    visit=set()
    while n not in visit:
        visit.add(n)
        n  = balance(n)
        if n==1:
            return True
        
    return False

def balance(n):
    o=0
    while n:
        o= o+ (n%10)**2
        n = n//10
    return o


def plusOne(digits):
    digits=digits[::-1]
    one=1
    i=0
    while one:
        if i <len(digits):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                one=0
        else:
            digits.append(1)
            one=0
        i=i+1
    return digits[::-1]

def myPow(x, n):
    num = abs(n)
    total=1
    while num>1:
        if num%2==0:
            x=x*x
            num=num//2
        else:
            total = total*x
            num=num-1
    return total * x if n>0 else 1/(total*x)
    
x = 2.00000; n = 10
print(myPow(x,n))
