"""in monkey sort  suppose there are  10 cards and a monkey is aked to sort those card , 
he will flips the card in air then check if cards are not sorted he again throws the card and 
checkk and continue"""


import random

def is_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            sorted = False
    return sorted
def monkey(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr
    
p = monkey([9,6,8,5,7,6])
print(p)

"tc: infinite"