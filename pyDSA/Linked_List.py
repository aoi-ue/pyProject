class Node: 
    def __init__(self,val):
        self.val = val 
        self.next = None 

class LinkedList: 
    def __init__(self): 
        self.head = None 

    def insert_head(self, new_val): 
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, new_val): 
        new_node = Node(new_val)

        if self.head is None: 
            self.head = new_node
            return 

        ref_node = self.head 

        while ref_node.next is not None: 
            ref_node = ref_node.next
        
        ref_node.next = new_node 

    def reverseList(self): 
        prev = None 
        curr_node = self.head
        next = curr_node.next 

        while curr_node:
            curr_node.next = prev 
            prev = curr_node
            curr_node = next 
            if next:
                next = next.next
        self.head = prev 

    def count_elements(self): 
        if self.head is None: 
            return 0 

        count = 0 

        while self.head is not None: 
            count += 1 
            self.head = self.head.next 

        return count 

    def print_linked_list(self): 
        if self.head is None:
            return ""

        node = self.head 
        while node is not None:
            print(node.val)
            node = node.next 

llist = LinkedList()

llist.insert_head('a')
llist.insert_end('b')
llist.insert_head('c')
llist.insert_end('d')

print(llist.count_elements())

# print (llist.print_linked_list())

# llist.reverseList() 
# print (llist.print_linked_list())