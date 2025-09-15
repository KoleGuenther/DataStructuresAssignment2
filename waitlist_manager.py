# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None
    
    
# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None
    
    def add_front(self, name):
        # Create a new node and add it to the front of the list
        # Skips the rest of the line, becoming the first node
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        # Create a new node and add it to the end of the list
        new_node = Node(name)
        if self.head is None: # If the list is empty, set the new node as the first node
            self.head = Node(name)
            return
        
        current = self.head
        while current.next: # Traverse to the end of the list
            current = current.next 
        current.next = new_node # Link the last node to the new node

    def remove(self, name):
        # Remove a node by name from the list
        if self.head is None: # If the list is empty, nothing to remove
            return
        
        # Case 1. Removing the Head Node
        if self.head.name == name:
            self.head = self.head.next
            return
        
        # Case 2. Search for the node to remove
        prev = None
        current = self.head
        while current and current.name != name:
            prev = current
            current = current.next

        if current: # If the node was found, unlink it from the list
            prev.next = current.next

    def print_list(self):
        # Print all names in the list
        current = self.head # Start from the head
        while current:
            print(current.name)
            current = current.next # Move to the next node


def waitlist_generator():
    # Create a new linked list instance
    
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?

The list works by having a Node, which includes two parts:
Data - the name of the customer
Link/Pointer - a reference to the next node in the list
Using both of these, we have the information of the customer, and who is next in line. Using this, we can add customers to the front or end of the list, remove them by name, and print the entire list.

The head points to the first node in the list. It is not the first node in the list. The head is a reference to the first node, which contains the data and a pointer to the next node. If the head is None, it means the list is empty. The head is crucial for the linkedlist to function.

A real engineer might need a custom list like this when they need to manage a collection of items where the size is not known in advance or changes often. A good example of this is a waitlist, like we created, whether for a restaurant, waiting room, concert tickets, or even a printing queue with priority. Custom lists make it easy to add or remove items without needing to shift elements around, as would be necessary in an array or standard list.
'''