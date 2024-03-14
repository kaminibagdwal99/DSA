"""hasing provides fast searching
1 . linear probing
"""


class Dictionary:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        return abs(hash(key))% self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] == None:
            self.slots[hash_value]=key
            self.data[hash_value]=value
        else:
            if self.slots[hash_value]==key:
                self.data[hash_value]=value
            else:
                newhash = self.rehash(hash_value)
                while self.slots[newhash]!= None and self.slots[newhash] != key:
                    newhash = self.rehash(newhash)

                if self.slots[newhash] ==None:
                    self.slots[newhash]=key
                    self.data[newhash]=value
                else: 
                    self.data[newhash]=value


    def rehash(self, old_hash):
        return (old_hash+1)%self.size

    def __setitem__(self,key,value):
        self.put(key,value)

    def get(self, key):
        start_position = self.hash_function(key)
        current_position = start_position

        while self.slots[current_position] != None:
            if self.slots[current_position] == key:
                return self.data[current_position]
            current_position = self.rehash(current_position)

            if current_position == start_position:
                return "item not found"

        return "item not found"

    

    def __getitem__(self,key):
        return self.get(key)

    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i]  != None:
                print(self.slots[i] ,":",self.data[i],end = " ")
        return ""



d = Dictionary(3)
d['python']=39
d.put('java', 89)
print(d.get('javaa'))
print(d['java'])
print(d)

