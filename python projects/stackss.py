class queue:
    def __init__(self):
        self.s=[]
    def enqueue(self,item):
        self.s.append(item)
    def dequeue(self):
        return self.s.pop(0)
    def is_empty(self):
        if self.s==[]:
            return True
        return False
res=queue()
res.enqueue("shadman")
res.enqueue("tahmid")
res.enqueue("hamza")
while not res.is_empty():
    print(res.dequeue())
    
