
class UF:
    def __init__(self,n):
        self.NoOfObjects = n
        self.setaya = list()
        for i in range(self.NoOfObjects):
            self.setaya.append({i})
    def find(self,p): 
        return next(x for x,y in enumerate(self.setaya) if p in y )
    def IsConnected(self,p,q):
        return self.find(q)==self.find(p)
        
    def union(self,p,q):
        if p < self.NoOfObjects and q <self.NoOfObjects and self.IsConnected(p,q) ==False:
            index1 = self.find(p)
            poping = [self.setaya.pop(index1)]
            index2 = self.find(q)
            poping.append(self.setaya.pop(index2))
            CombinedSet = set()
            for i in poping:
                CombinedSet.update(i)
            self.setaya.append(CombinedSet)
            
            
    def count(self):
        return len(self.setaya)
