""" Creating a linked list and implenting print, append, prepend, insert_after_node, insert_before_node, delete, delete_head and delete_last methods with it """

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

        """ 
        This snipet of code checks if the given node is the last of the linked list and implements append method if true.
        This code is not needed.

        last_node = self.head

        while last_node.next:
            
            last_node = last_node.next 

        if previous_node is last_node:

            self.append(data)

            print('yes')

            return 
            
        """

        new_node = Node(data)

        new_node.next = previous_node.next

        previous_node.next = new_node


    def insert_before_node(self, next_node, data):

        """ Add the new node before the given node """

        if not next_node:

            print('Given not does not exist :(')

            return

        new_node = Node(data)

        last_node = self.head

        previous_node = None

        while last_node:

            if next_node is last_node:# Matching given node against all the nodes in the linked list one by one

                if previous_node is None: #Check if given node is the head of the linked list

                    self.preprend(data)

                    return

                else:

                    previous_node.next = new_node
                    new_node.next = last_node

                    return

            previous_node = last_node
            last_node = last_node.next

    def delete_after_node(self, previous_node):

        """ Delete the node that is after the given node """
        if not previous_node.next: #If given node if null

            print('There is no node after the given node :(')

            return

        last_node = self.head

        while last_node:

            if previous_node is last_node: #Matching previous node against linked list nodes

                previous_node.next = last_node.next.next #Assigning the the node present after the deleted node

                return

            last_node = last_node.next


    def delete_head(self):

        """ Delete the head (first) node of the linked list """
        self.head = self.head.next

    def delete_last(self):

        """ Delete the last node of the linked list """
        last_node = self.head

        while last_node.next.next:# Stopping the iterator on the 2nd last node

            last_node = last_node.next

        last_node.next = None #Deleting the reference of last node from 2nd last node

    def delete(self, node):

        """ Delete the given node in the linked list """
        if not node:

            print('Given node does not exist :(')

            return

        last_node = self.head
        previous_node = None #Keeping a trace of the node present before the node to be deleted

        while last_node:

            if node is last_node:

                if previous_node is None: #Check if the node to be deleted is the head of the linked list

                    self.delete_head()

                    return

                else:

                    previous_node.next = last_node.next

                    return
            
            previous_node = last_node
            last_node = last_node.next     

linked_list = LinkedList()
linked_list.append("1")
linked_list.append("2")
linked_list.preprend("0")
linked_list.insert_after_node(linked_list.head.next, 9)
linked_list.insert_before_node(linked_list.head, "4")
linked_list.insert_before_node(linked_list.head.next, "5")
linked_list.insert_before_node(linked_list.head.next.next.next.next.next, "11")
linked_list.print()
print('...')
linked_list.delete_head()
linked_list.print()
print('...')
linked_list.delete_last()
linked_list.print()
print('...')
linked_list.delete(linked_list.head.next.next.next.next)
linked_list.print()
print('...')
linked_list.insert_before_node(linked_list.head.next.next.next, "100")
linked_list.print()
print('...')
linked_list.delete(linked_list.head.next.next.next.next)
linked_list.print()
print('...')
linked_list.delete_after_node(linked_list.head.next.next.next)
linked_list.print()