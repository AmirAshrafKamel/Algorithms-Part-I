class QuickFindUF:
    def __init__(self,n):
        self.n = n
        self.lista = list(range(n))
    def IsConnected(self,p,q):
        return self.lista[p] == self.lista[q]
    def union(self,p,q):
        if p < self.n and q < self.n and self.IsConnected(p,q) == False:
            for i in range(self.n):
                if self.lista[i] == self.lista[q]:
                    self.lista[i] = self.lista[p]
        print(self.lista)


