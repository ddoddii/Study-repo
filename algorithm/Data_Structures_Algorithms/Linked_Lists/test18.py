# Linked List : Remove Duplicates
# Removes all duplicate values from list



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next  
            
    def print_all(self):
        if self.length == 0:
            print("Head: None")
        else:
            print("Head: ", self.head.value)
        print("Length: ", self.length)
        print("\nLinked List:")
        if self.length == 0:
            print("empty")
        else:
            self.print_list()

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

# 처음에는 values 에 아무것도 없기 때문에 else 가 먼저 실행된다.
# 여기서 prev = curr , 즉 현재 head 로 이동한다
# curr = curr.next 를 통해 curr 는 항상 한칸 옆으로 이동한다
# 만약 curr.value 가 values 안에 있다면 prev.next = curr.next 를 통해 현재 curr 는 사라진다 
# curr 이 하나 사라지면 length 를 하나 줄인다
    def remove_duplicates(self):
        values = set()
        prev = None
        curr = self.head
        while curr:
            if curr.value in values:
                prev.next = curr.next
                self.length -= 1
            else:
                values.add(curr.value)
                prev = curr
            curr = curr.next
        
    



my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()


my_linked_list.print_all()




"""
    EXPECTED OUTPUT:
    ----------------
    Head:  1
    Length:  4
    Linked List:
    1
    2
    3
    4
    
"""
