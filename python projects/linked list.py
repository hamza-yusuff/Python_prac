class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    def __repr__(self):
        return repr(self.data)
class Linkedlist:
    def __init__(self):
        self.head=Node()
    def __repr__(self):
        nodes=[]
        current_node=self.head.next
        while current_node:
            nodes.append(current_node)
            current_node=current_node.next
        return ' '.join(nodes)
    def preprand(self,data):
        node=Node(data,self.head.next)
        self.head.next=node
    def append(self,data):
        current_node=self.head.next
        if not current_node:
            node=Node(data,self.head.next)
            self.head.next=node
            return
        while current_node:
            current_node=current_node.next
        node=Node(data,current_node)
        current_node.next=node
    def search(self,item):
        current_node=self.head.next
        if not current_node:
            return "NOT FOUND"
        while current_node:
            if current_node.data==item:
                return repr(current_node)
            current_node=current_node.next
        else:
            return None
    def remove(self,data):
        previous_node=self.head
        current_node=self.head.next
        if not current_node:
            return None
        while current_node:
            if current_node.data==data:
                previous_node.next=current_node.next
                return
            current_node=current_node.next
        else:
            return None
    def insert(self,data,new):
        previous_node=self.head
        current_node=self.head.next
        if not current_node:
            node=Node(new,self.head.next)
            self.head.next=node
            return
        while current_node:
            if current_node==data:
                node=Node(new,current_node.next)
                current_node.next=node
                return
            current_node=current_node.next
        else:
            return None
