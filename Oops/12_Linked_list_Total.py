class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def printLL(self):
        current = self.head 
        while current:
            print(current.val, end = "- >")
            current = current.next 

        print(None)

    def LL_size(self):
        size = 0 
        current = self.head 
        while current:
            size += 1 
            current = current.next 

        return size
    def get(self, index: int) -> int:
        size = self.LL_size()
        
        if index >= size or index < 0:
            return -1

        if index == 0:
            return self.head.val 

        else:
            current = self.head
            for i in range(index):
                current = current.next 
            return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head 
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        current = self.head 

        if self.head is None:
            self.head = new_node 
            return
            
        while current.next:
            current = current.next 

        current.next = new_node 
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        size = self.LL_size()

        if index < 0 or index > size:
            return 

        if index == 0:
            self.addAtHead(val)
            return 

        elif index ==  size:
            self.addAtTail(val)
            return 

        else:
            current = self.head 
            for i in range(index-1):
                current = current.next

            temp = current.next 
            current.next = new_node 
            new_node.next = temp
            

    def deleteAtIndex(self, index: int) -> None:
        size = self.LL_size()

        if index < 0 or index >= size:
            return 

        elif index == 0:
            self.head = self.head.next
            return 

        elif index == size-1:
            current = self.head 
            for i in range(index-1):
                current = current.next 

            current.next = None 
            return 

        else:
            current = self.head 
            for i in range(index-1):
                current = current.next 

            current.next = current.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(1)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.deleteAtIndex(1)