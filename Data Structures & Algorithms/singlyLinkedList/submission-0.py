class LinkedList:
    
    def __init__(self):
        self._head = None
        self.nodes = []

    
    def get(self, index: int) -> int:
        curr = self._head
        count = 0 
        while curr is not None:
            if count == index:
                return self.nodes[curr][0]
            curr = self.nodes[curr][1]
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        self.nodes.append([val, self._head])
        self._head = len(self.nodes) - 1

    def insertTail(self, val: int) -> None:
        new_index = len(self.nodes)
        self.nodes.append([val, None])
        if self._head is None:
            self._head = new_index
            return
        curr = self._head
        while self.nodes[curr][1] is not None:
            curr = self.nodes[curr][1]
        self.nodes[curr][1] = new_index

    def remove(self, index: int) -> bool:
            if index == 0:
                if self._head is None:
                    return False
                self._head = self.nodes[self._head][1]
                return True
            curr = self._head
            prev = curr
            curr = self.nodes[curr][1]
            count = 1
            while curr is not None:
                if count == index:
                    self.nodes[prev][1] = self.nodes[curr][1]
                    return True
                prev = curr
                curr = self.nodes[curr][1]
                count += 1
            return False

    def getValues(self) -> List[int]:
        vals = []
        curr = self._head
        while curr is not None:
            vals.append(self.nodes[curr][0])
            curr = self.nodes[curr][1]
        return vals        
