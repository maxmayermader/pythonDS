class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head =  new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
        #################################
        # FINISH WRITING APPEND METHOD  #
        # INSERT IF/ELSE STATEMENT HERE #
        #################################
        
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = temp
        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next= None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if self.length <= index or index < 0:
            return None
        currNode = self.head
        for _ in range(index):
            currNode = currNode.next
        return currNode

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index >= self.length or index < 0:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()

        pre = self.get(index-1)
        temp = self.get(index)

        pre.next = temp.next
        temp.next = None

        self.length -= 1

        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        fp = self.head
        sp = self.head
        while fp != None:
            fp = fp.next.next
            sp = sp.next

        return sp

    def reverse_between(self, m, n):
        if self.length <= 1:
            return

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for i in range(m):
            prev = prev.next

        current = prev.next

        for i in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        self.head = dummy.next
        # i = m
        # j = n
        # while i != j:
        #     mNode = self.get(i)
        #     temp = mNode.value
        #     nNode = self.get(j)
        #     # print(mNode.value)
        #     # print(nNode.value)
        #     mNode.value = nNode.value
        #     nNode.value = temp
        #     # print(mNode.value)
        #     # print(nNode.value)
        #     i += 1
        #     j -= 1

###############TEST######################


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()

# my_linked_list = LinkedList(1)
# my_linked_list.make_empty()
#
# my_linked_list.append(1)
# my_linked_list.append(2)
#
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length, '\n')
#
# print('Linked List:')
# my_linked_list.print_list()
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     Head: 1
#     Tail: 2
#     Length: 2
#
#     Linked List:
#     1
#     2
#
# """
#
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
#
# print('LL before reverse():')
# my_linked_list.print_list()
#
# my_linked_list.reverse()
#
# print('\nLL after reverse():')
# my_linked_list.print_list()
#
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
#
# print( my_linked_list.find_middle_node().value )