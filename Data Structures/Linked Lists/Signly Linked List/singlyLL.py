""" Creating a linked list and implenting print, append, prepend and insert_after_node methods with it """

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def print(self):

        """ Prints data at all nodes in generated linked list in sequence """
        current_node = self.head

        while current_node:

            print(current_node.data)

            current_node = current_node.next

    def append(self, data):

        """ Add the node at the end of generated linked list """
        new_node = Node(data)

        if self.head is None: #Check if the linked_list is empty

            self.head = new_node

            return

        last_node = self.head

        while last_node.next: #Check if the linked list has more nodes, until the last node

            last_node = last_node.next

        last_node.next = new_node

    def preprend(self, data):

        """ Add the new node at the start of the generated linked list, that is making it the head of the linked list """

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def insert_after_node(self, previous_node, data):

        """ Add the new node after the given node """

        if not previous_node:

            print('Given node does not exist :(')

            return

        new_node = Node(data)

        new_node.next = previous_node.next

        previous_node.next = new_node
    
linked_list = LinkedList()
linked_list.append("1")
linked_list.append("2")
linked_list.preprend("0")
linked_list.insert_after_node(linked_list.head.next, 9)
linked_list.print()

