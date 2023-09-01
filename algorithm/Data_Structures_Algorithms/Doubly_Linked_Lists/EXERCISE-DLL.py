# Doubly Linked List

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            # 연결이 양방향이므로 2가지 다 제거해야 한다 (next, prev)
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index > self.length / 2:
            temp = self.tail 
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_value(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        before.next = new_node
        new_node.prev = before
        after.prev = new_node
        new_node.next = after
        self.length += 1   
        return True 

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
        

my_doublylinked_list = DoublyLinkedList(1)
my_doublylinked_list.append(3)
my_doublylinked_list.append(5)
my_doublylinked_list.append(7)

my_doublylinked_list.prepend(10)

print("get idx:", my_doublylinked_list.get(4).value)
my_doublylinked_list.set_value(1,2)
my_doublylinked_list.insert_value(1,4)
print("Original list:")
my_doublylinked_list.print_list()
print("remove idx:", my_doublylinked_list.remove(0))
print("remove idx:", my_doublylinked_list.remove(2).value)

my_doublylinked_list.print_list()