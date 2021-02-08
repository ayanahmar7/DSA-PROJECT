class ResizeableArray:
    """An Array Based List Implementation Which Dynamically Changes Its Size When An Element Is Added
Or Removed From An Array."""
    def __init__(self):
        self.capacity = 1 #Intitial capacity that can vary
        self.size = 0
        self.array = self.createArray(self.capacity)

    def print(self):
        print(self.array)

    def createArray(self,capacity):
        return [None] * self.capacity #Creates an array with an specific capacity

    def empty(self):
        if self.size==0: #Checking the if a list is empty
            return True
        return False

    def full(self):
        if self.size == self.capacity: #Checking when an array is full
            return True
        return False

    def get(self,i):
        if i < 0 or i >=self.size: #Bounds checking for array
            raise IndexError("Index Out Of Range")
        return self.array[i] #Returning element at specific index

    def set(self,i,x):
        if i < 0 or i >= self.size: #Bounds checking for array
            raise IndexError("Index Out Of Range")
        value=self.array[i]
        self.array[i]=x #Updating Value at specific index
        return value #Returning old value

    def add(self,i,x):
        if  i < 0 or i >self.size:
            raise IndexError("Index Out Of Range")
        if self.full():
            self.resize() #Growing an array when it reaches it capacity
        for j in range(self.size, i,-1):
            self.array[j] = self.array[j - 1] #Shifting elements to make space for new element
        self.array[i] = x
        self.size += 1 #Incrementing size

    def remove(self,i):
        if  i < 0 or i >= self.size:
            raise IndexError("Index Out Of Range")
        if self.empty():
            print("Cant remove from an empty array")
        for j in range(self.size):
            if j == i:
                for k in range(j, self.size - 1):
                    self.array[k] = self.array[k + 1] #Shifting elements rightwards to fill empty space in array
                self.array[self.size - 1] = None
                self.size -= 1
            if self.size <= self.capacity // 2: #Shrinking an array when it is half of capacity
                self.shrink()

    def resize(self):
        rsz_array=2*self.createArray(self.capacity) #Array grows double the capacity
        for i in range(self.size):
            rsz_array[i]=self.array[i] #Copying elements from array to bigger array
        self.array=rsz_array #Making bigger array our new array
        self.capacity=len(rsz_array)

    def shrink(self):
        rsz_arr = []
        for i in range(len(self.array)):
            if self.array[i]:
                rsz_arr.append(self.array[i]) #Appending to array till all elements are being done
        self.capacity = (self.capacity * 50 // 100)
        self.array = self.createArray(self.capacity) #Creating an array half of the old capacity
        self.array = rsz_arr #Making smaller array our new array
obj=ResizeableArray()
print("--Array Inititally--")
obj.print()
obj.add(0,1)
obj.add(1,7)
obj.add(2,9)
obj.add(2,10)
print("--Array After Insertion--")
obj.print()
obj.remove(0)
obj.remove(2)
print("--Array After Deletion--")
obj.print()
print("--Getting An Element--")
print(obj.get(0))
print("--Set An Element--")
obj.set(0,19)
obj.print()

