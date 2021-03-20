def makelist(info):
    if len(info)==1:
        return info
    else:
        return makelist(info[1:])+[info[0]]

def no_duplicate(lists):
    
    f=[]
    def dynamic(info):
        if len(info)==1:
            if info[0] in f:
                return []
            return info
        elif info[0] in f:
            return dynamic(info[1:])
        
        else:
            f.append(info[0])
            return [info[0]]+dynamic(info[1:])
    return dynamic(lists)

