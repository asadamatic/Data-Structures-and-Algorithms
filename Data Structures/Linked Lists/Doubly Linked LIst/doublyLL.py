""" Implementation of Doubly Linked List in pyhon along with it's functions
print_forward, print_reverse,
append, prepend, 

"""

class Node:

    def __init__(self, data):

        self.data = data
        self.previous = None
        self.next = None
        
class LinkedList:

    def __init__(self):

        self.head = None

    def print_forward(self):

        """ Printing linked list starting from head"""
        pointer = self.head

        while pointer:

            print(pointer.data)

            pointer = pointer.next

    def print_reverse(self):

        """ Printing linked list in reverse """
        pointer = self.head

        while pointer.next:

            pointer = pointer.next

        while pointer:

            print(pointer.data)

            pointer = pointer.previous

    def append(self, data):

        """ Adding a newnode at the end of the linked list """
        new_node = Node(data)

        if self.head is None:

            self.head = new_node
            return

        pointer = self.head #Iterator for the linked list
        
        while pointer.next:

            pointer = pointer.next            

        pointer.next = new_node
        new_node.previous = pointer

    def prepend(self, data):

        """ Adding a new node at the beginning of the linked list """
        new_node = Node(data)

        self.head.previous = new_node

        new_node.next = self.head
        
        self.head = new_node

    def insert_after_node(self, previous_node, data):

        """ Adding a new node after the given not """
        if not previous_node:

            print('The given node does not exist :(')
            return
        
        if not previous_node.next:

            self.append(data)
            return

        new_node = Node(data)
        previous_node.next.previous = new_node
        new_node.next = previous_node.next
        previous_node.next = new_node
        new_node.previous = previous_node
        

    def insert_before_node(self, next_node, data):

        if not next_node:

            print('The given node does not exist :(')
            return

        if not next_node.previous:

            self.prepend(data)
            return
            
        new_node = Node(data)

        next_node.previous.next = new_node
        new_node.previous = next_node.previous
        new_node.next = next_node
        next_node.previous = new_node
        

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.prepend(3)
linked_list.prepend(4)

linked_list.insert_before_node(linked_list.head, 7)
linked_list.print_forward()
print("..............................")
linked_list.print_reverse()
