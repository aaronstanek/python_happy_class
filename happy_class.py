class happy_class:
    def __setitem__(self,key,value):
        setattr(self,key,value)
    def __getitem__(self,key):
        return getattr(self,key)
    def __delitem__(self,key):
        delattr(self,key)
    def __contains__(self,key):
        if hasattr(self,key):
            return True
        return False

def mklist(obj):
    w = dir(obj)
    ou = []
    for x in w:
        if x[:2]!="__":
            ou.append(x)
    return ou
