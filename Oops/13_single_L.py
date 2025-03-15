class N_node:
    def __init__(self,val):
        self.val = val
        self.next = None

class L_link:
    def __init__(self):
        self.head = None

    def Continue(self):
        current = self.head
        while current:
            print(current.val,end = " ")
            current = current.next


n1 = N_node(10)
n2 = N_node(20)
n3 = N_node(30)

head = L_link()
head.head = n1

n1.next = n2
n2.next = n3
n3.next = None

head.Continue()



