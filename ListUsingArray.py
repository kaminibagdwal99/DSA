import ctypes

class MyList:

    def __init__(self) -> None:
        self.size = 1
        self.n = 0

        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        # createa a ctype static array with size capacity and its a referential arrar
        return (ctypes.py_object * capacity)()

     
    def __len__(self):
        return self.n

    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size*2)

        #append    

        self.A[self.n]=item
        self.n = self.n+1

    def __resize(self, new_capacity):
        # create new array
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copy content

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B

    def __str__(self) -> str:
        result = ""
        for i in range(self.n):
            result = result +str(self.A[i])+','
        return  '[' +result[:-1]+']'


    def __getitem__(self, index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            return "index Error: index out of range"

    def pop(self):
        if self.n ==0:
            return "Empty List"
        print(self.A[self.n-1])
        self.n = self.n-1

    def clear(self):
        self.n = 0
        self.size =1

    def find(self,item ):
        for i in range(self.n):
            if self.A[i]==item:
                return i
        return "value Error - not in list"

    def insert(self, pos, item):

        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]

        self.A[pos]=item
        self.n = self.n +1

    def __delitem__(self,pos):
        if 0<=pos<self.n:

            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
            self.n = self.n-1

    def remove(self,value):
        pos = self.find(value)

        if type(pos )==int:
            self.__delitem__(pos)
        else:pos


L = MyList()
print(type(L))
L.append("hello")
L.append("world")


print(L)
L.remove("hell")
print(L)




