class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def PrintLl(self):
        current = self.head
        if current is None:
            print("It is Empty Linked List...")
        else:
            while current: 
                print(current.val,end = "  ")
                current = current.next
    

L = LinkedList()

n1 = Node(10)
L.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3

L.PrintLl()


