class UFCanonicalElement:
    def __init__(self,n):
        self.n = n
        self.components = list(range(n))
        self.biggest =list(range(n))
        self.size = [1]*n
        print(self.biggest)
        
    def root(self,i):
        if self.components[i]!= i:
            self.components[i] = self.root(self.components[i])
        return i
    def find(self,i):
        return self.biggest[self.root(i)]
    def union(self,p,q):
        rootp = self.root(p)
        rootq = self.root(q)
        if rootp != rootq:
            if self.size[rootp]>self.size[rootq]:
                self.components[rootq] = self.components[rootp]
                self.biggest[rootp] = max(self.biggest[rootp],self.biggest[rootq])
                self.size[rootp] +=self.size[rootq]
            else:
                self.components[rootp] = self.components[rootq]
                self.biggest[rootq] = max(self.biggest[rootq],self.biggest[rootp])
                self.size[rootq] +=self.size[rootp]
    
UFCanonicalElement(7)