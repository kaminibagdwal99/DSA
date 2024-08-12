from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity = 0) :
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    


    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        if len(self.cache)>= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key]=value


obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))