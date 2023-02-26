# Implementaion using Sentinal node
# It'll always be present as a head. Wont count towards Size. So the next node of sentinal node would have index 0.
# Value of sentinal node is set to 0. line 13.
# Thats why in method printList(), the curr was set to head.next as head is sentinal node.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next 
        pred.next = pred.next.next

    def printLinkedList(self):
        curr = self.head.next                   #self.head is sentinal node
        while(curr!= None):
            print(curr.val,"--> ", end = '')
            curr = curr.next
    


naikaj=MyLinkedList()
#naikaj.addAtHead(0)
naikaj.addAtHead(3)
naikaj.addAtHead(2)
naikaj.addAtHead(1)
#naikaj.printLinkedList()
#print(naikaj.get(1))
# naikaj.deleteAtIndex(1)
# naikaj.addAtIndex(1,2)
# naikaj.addAtTail(4)
# naikaj.printLinkedList()
print(naikaj.size)
print(naikaj.head.val)
naikaj.printLinkedList()
print(naikaj.head.val)





