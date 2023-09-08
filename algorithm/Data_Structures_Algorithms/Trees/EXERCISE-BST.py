class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        else:
            curr = self.root
            while curr is not None:
                if new_node.value == curr.value:
                    return False
                if value < curr.value:
                    if curr.left is None:
                        curr.left = new_node
                        return True
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = new_node
                        return True
                    curr = curr.right

    def contains(self,value):
        curr = self.root
        while curr is not None:
            if curr.value == value:
                return True
            if value < curr.value:
                if curr.left is None:
                    return False
                curr = curr.left
            else: 
                if curr.right is None:
                    return False
                curr = curr.right
        return False
            

        
my_tree  = BinarySearchTree()
print(my_tree.contains(52))
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(52)

print(my_tree.contains(52))



print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.left.left.value)
print(my_tree.root.right.value)
print(my_tree.root.right.left.value)


