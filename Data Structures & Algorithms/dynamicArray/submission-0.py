class DynamicArray:
    
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._array = [None] * capacity
        self._size = 0

    def get(self, i: int) -> int:
        assert 0 <= i < self._size
        item = self._array[i]
        assert item is not None
        return item

    def set(self, i: int, n: int) -> None:
        assert 0 <= i < self._size
        self._array[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self._array[self._size] = n
        self._size += 1
        

    def popback(self) -> int:
        assert self._size > 0
        val = self._array[self._size - 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return val

    def resize(self) -> None:
        new_capacity = self._capacity * 2
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def getSize(self) -> int:
        return self._size
        
    def getCapacity(self) -> int:
        return self._capacity
