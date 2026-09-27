class List_node:
    def __init__(self,a,next_=None):
        self.val=a
        self.next=next_
class Linked_list:
    def __init__(self,head=None):
        self.head=head
    def trav(self):
        cur=self.head
        while cur is not None:
            print(cur.val)
            cur=cur.next
    def append(self,val):
        if self.head is None:
            self.head=List_node(val)
            return
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        
        cur.next=List_node(val)
l=Linked_list()
l.append(1)
l.append(23)
l.append(4)                
l.trav()