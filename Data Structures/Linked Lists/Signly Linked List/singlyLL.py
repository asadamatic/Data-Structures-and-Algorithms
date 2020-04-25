""" Implementation of Singly linked list in python with implementation of these functions
 print,
 append, prepend, insert_after_node, insert_before_node,
 delete_after_node, delete_before_node,delete, delete_head, delete_last, delete_node_with_data,
 length_iterative, length_recursive,
 swap_node_data, swap_nodes, swap_nodes_with_data,
 reverse_list

methods with it """

# pointer is iterator on the linked list till the last node
class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def print(self):

        """ Prints data at all nodes in generated linked list in sequence """
        pointer = self.head

        while pointer:

            print(pointer.data)
            pointer = pointer.next

    def append(self, data):

        """ Add the node at the end of generated linked list """
        new_node = Node(data)

        if self.head is None: #Check if the linked_list is empty

            self.head = new_node
            return

        pointer = self.head

        while pointer.next: #Check if the linked list has more nodes, until the last node

            pointer = pointer.next

        pointer.next = new_node

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

    def insert_before_node(self, next_node, data):

        """ Add the new node before the given node """
        if not next_node:

            print('Given not does not exist :(')
            return

        if next_node is self.head:

            self.preprend(data)
            return

        new_node = Node(data)
        pointer = self.head
        previous_node = None

        while pointer:

            if next_node is pointer:# Matching given node against all the nodes in the linked list one by one

                if previous_node is None: #Check if given node is the head of the linked list

                    self.preprend(data)
                    return

                else:

                    previous_node.next = new_node
                    new_node.next = pointer
                    return

            previous_node = pointer
            pointer = pointer.next

    def delete_after_node(self, previous_node):

        """ Delete the node that is after the given node """
        if not previous_node:

            print('The given node does not exist :(')
            return

        if not previous_node.next: #If given node if null

            print('There is no node after the given node :(')
            return

        previous_node.next = previous_node.next.next
    
    def delete_before_node(self, next_node):

        if not next_node:

            print('This node does not exist :(')
            return

        if next_node is self.head:

            print('There is no node before this node :(')
            return

        pointer = self.head
        previous_node = None

        while pointer.next:

            if next_node is pointer.next:

                if previous_node is None:

                    self.head = pointer.next
                    return

                else:

                    previous_node.next = pointer.next
                    return

            previous_node = pointer
            pointer = pointer.next

    def delete_head(self):

        """ Delete the head (first) node of the linked list """
        self.head = self.head.next

    def delete_last(self):

        """ Delete the last node of the linked list """
        pointer = self.head

        while pointer.next.next:# Stopping the iterator on the 2nd last node

            pointer = pointer.next

        pointer.next = None #Deleting the reference of last node from 2nd last node

    def delete(self, node):

        """ Delete the given node in the linked list """
        if not node:

            print('Given node does not exist :(')
            return

        pointer = self.head
        previous_node = None #Keeping a trace of the node present before the node to be deleted

        while pointer:

            if node is pointer:

                if previous_node is None: #Check if the node to be deleted is the head of the linked list

                    self.delete_head()
                    return

                else:

                    previous_node.next = pointer.next
                    return
            
            previous_node = pointer
            pointer = pointer.next

    def delete_node_with_data(self, data): #Assuming that all the nodes have uniqure data

        """ Deleting the node containing that contains the given data """

        pointer = self.head
        node_check = None
        previous_node = None
        
        while pointer:

            if data is pointer.data:
                
                node_check = pointer

                if previous_node is None:

                    self.head = pointer.next
                    return

                else:

                    previous_node.next = pointer.next
                    return

            previous_node = pointer
            pointer = pointer.next

        if node_check is None:

            print('Node with the given data does not exist :(')
            return

    def length_iterative(self):

        """ calculating the length of linked list by iterating on the list"""
        pointer = self.head
        length = 0

        while pointer:

            length = length + 1    
            pointer = pointer.next 
        
        return length

    def length_recursive(self, node):

        """ Calculating the length of linked list using recurrsion """
        
        if node is None:

            return 0

        return 1 + self.length_recursive(node.next)

    def swap_nodes_data(self, first_node, second_node):

        """ Swaping data of the given nodes """ 

        if not first_node and not second_node:

            print('Either first or second node does not exist :(')
            return

        temporary_data = first_node.data
        first_node.data  = second_node.data
        second_node.data = temporary_data

    def swap_nodes(self, first_node, second_node):

        """ Swaping the given nodes """
        if not first_node and second_node:

            print('Either first or second node does not exist :(')
            return

        node_first = self.head
        previous_first = None

        while node_first.next:

            if node_first.next is first_node:
            
                previous_first = node_first
                break

            node_first = node_first.next

        node_second = self.head
        previous_second = None

        while node_second.next:

            if node_second.next is second_node:

                previous_second = node_second
                break

            node_second = node_second.next

        temporary_next = second_node.next

        if previous_first is None:
            
            self.head = second_node

        else:

            previous_first.next = second_node

        if first_node.next is second_node:

            second_node.next = first_node
        
        else:
            
            second_node.next = first_node.next

        if previous_second is None:

            self.head = first_node

        else:

            previous_second.next = first_node

        if first_node.next is second_node:

            first_node.next = second_node
        
        else:

            first_node.next = temporary_next

    def swap_nodes_with_data(self, first_data, second_data):

        """ Swaping two nodes whose data is given """
        pointer = self.head
        first_node = None

        while pointer.next:

            if first_data is pointer.data:

                first_node = pointer

            pointer = pointer.next

        
        pointer = self.head
        second_node = None

        while pointer.next:

            if second_data is pointer.data:

                second_node = pointer

            pointer = pointer.next

        if first_node is None or second_node is None:

            print('Node with the given data does not exist :(')
            return

        self.swap_nodes_data(first_node, second_node)

    def reverse_list(self):

        """ Reversing the linked list """
        pointer = self.head

        previous_node = None
        older_node = None

        while pointer:
            
            if previous_node is None:

                pass
                
            else:

                previous_node.next = older_node
                older_node = previous_node   

            
            if not pointer.next:

                pointer.next = older_node
                break
                
            previous_node = pointer
            pointer = pointer.next

        self.head = pointer
            

linked_list = LinkedList()
linked_list.append("1")
linked_list.append("2")
linked_list.preprend("0")
linked_list.insert_after_node(linked_list.head.next, 9)
linked_list.print()
linked_list.delete_after_node(linked_list.head.next.next)
print("______________________________________________________")
linked_list.print()
linked_list.reverse_list()
print("______________________________________________________")
linked_list.print()