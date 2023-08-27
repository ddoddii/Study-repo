# Partition List
# x 를 받아서 x 보다 작으면 dummy1 뒤에 연결하고, 크면 dummy2 뒤에 연결한다
# 마지막에 두개 리스트를 연결할 때는 prev1.next = dummy2.next 로 연결한다

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self,x):
        if self.head is None:
            return None
        dummy1 , dummy2 = Node(0) , Node(0)
        prev1 = dummy1
        prev2 = dummy2
        curr = self.head
        while curr is not None:
            if curr.value < x:
                prev1.next = curr
                prev1 = curr
            else:
                prev2.next = curr
                prev2 = curr
            curr = curr.next
        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next
        self.head = dummy1.next
        
    
    

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)


print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""
