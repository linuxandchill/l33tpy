class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head 

    def unshift(self, value):
        node = Node(value)

        if self.head is not None:
            temp = self.head
            self.head = node
            self.head.next_node = temp
        else:
            self.head = node

    def shift(self):
        if self.head is None:
            return "Empty"
        
        temp = self.head
        self.head = None
        self.head = temp.next_node 

mylist = LinkedList()
mylist.unshift(50)
mylist.unshift(60)
print(mylist.head.value)
mylist.shift()
print(mylist.head.value)
# print(mylist.head.next_node.value)
# print(mylist.tail)
# mylist.unshift(12)
# print(mylist.head.value)
# print(mylist.tail)
# mylist.push(30)
# print(mylist.head.value)
# print(mylist.tail)