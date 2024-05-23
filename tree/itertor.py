"""own for loop"""


def customise_loop(iterable):
    iter_iten= iter(iterable)

    while True:
        try:
            print(next(iter_iten))
        except StopIteration:
            break

a = [1,2,3]
customise_loop(a)

"""own range function"""

class OwnRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self)

class MyRangeIterator:
    def __init__(self, iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        current = self.iterable.start
        self.iterable.start += 1
        return current

for i in OwnRange(1,10):
    print(i)

