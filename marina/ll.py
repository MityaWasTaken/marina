class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
            
    def Insert(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
        
    def Remove(self, remove):
        Head = self.head
        if Head is not None:
            if Head.data == remove:
                self.head = Head.next
                Head = None
                return
        while Head is not None:
            if Head.data == remove:
                break
            prev = Head
            Head = Head.next
        
        if Head == None:
            return

        prev.next = Head.next
        Head = None
    
    def Search(self, search):
        current = self.head
        while current != None:
            if current.data == search:
                return True
            current = current.next
        return False
    
    def Print(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next
    
    def __findlength(self, h):
      
        curr = h
        cnt = 0
        while (curr != None):
        
            cnt = cnt + 1
            curr = curr.next
        
        return cnt
                
    def convertArray(self):
        len1 = self.__findlength(self.head)
        arr = []
    
        index = 0
        curr = self.head
        while (curr != None): 
            arr.append( curr.data)
            curr = curr.next
        
        return "\n".join(arr)