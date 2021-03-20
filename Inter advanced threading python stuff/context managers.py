from contextlib import contextmanager

@contextmanager
def file(filename,method):
    print("enter")
    file=open(filename,method)
    yield file
    print("exit")
    file.close()

with file("text.text","w") as f:
    print("middle")
    f.write("hello")
    

class File:
    def __init__(self,filename,method):
        self.file= open(filename,method)

    def __enter__(self):
        print("enter")
        return self.file

    def __exit__(self,type,value,traceback):
        print(type,value,traceback)
        print("Exit")
        self.file.close()
        if type == Exception:
            return True
        
with File("file.txt", "w") as f:
    print("Middle")
    f.write("hello")
    
    raise TypeError()
