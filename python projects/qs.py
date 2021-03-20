class stack:
    def __init__(self,string):
        self.word=list(string)
    def add(self,s):
        self.word.append(s)
    def out(self):
        k=self.word.pop()
        return k
class queue:
    def __init__(self,string):
        self.word=list(string)
    def dhuka(self,s):
        self.word.append(s)
    def remove(self):
        self.word.pop(0)
    def output(self):
        print(self.word)
sent=stack("hello")
palindrome=queue([])
for i in range(5):
    f=sent.out()
    palindrome.dhuka(f)
palindrome.output()
