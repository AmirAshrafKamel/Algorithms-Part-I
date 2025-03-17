class WeightedQuickUnionUF:
    def __init__(self,n):
        self.n = n
        self.lista = [x for x in range(n)]
        self.height = [1]*n

    def find(self,p):
        if self.lista[p]!= p:
            self.lista[p] = self.find(self.lista[p])    
        return self.lista[p]
    def IsConnected(self,p,q):
        return self.find(p) == self.find(q)
    def union(self,p,q):
        if p< self.n and q< self.n and self.IsConnected(p,q) == False: 
            i = self.find(p)
            j = self.find(q)
            if self.height[i]>self.height[j]:
                self.lista[j]= self.lista[i]
                self.height[i]+=self.height[j]
            else:
                self.lista[i]= self.lista[j]
                self.height[j]+=self.height[i]

        
