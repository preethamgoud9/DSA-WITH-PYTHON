class MyArray:
    def __init__(self,capacity=10):
        "Initializing the Array with fixed capacity of 10 here"
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def append(self,element):
        "Add an element to the array."
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = element
        self.size += 1
        

    def _resize(self):
        "Resize the array when it is full"
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def __getitem__(self,index):
        "Access an element by element"
        if index > self.size or index <= 0:
            raise IndexError("Index is out of range")
        return self.array[index]
    
    def __setitem__(self,index,value):
        "set an element at the specified value"
        if index > self.size or index <= 0:
            raise IndexError("Index is out of range")
        self.array[index] = value
    
    def len(self):
        "Return the current size of the array(Number of elements)"
        return self.size

    def str(self):