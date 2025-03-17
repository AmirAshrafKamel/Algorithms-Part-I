class Percolation:
    def __init__(self,n):
        self.n = n
        self.blocks = list(range((n**2)+2))
        self.IsOpened = [False]*((n**2)+2)
        self.NoOfOpenSites = 0
        self.size = [1]*((n**2)+2)
        self.VirtualTop = n**2
        self.VirtualBottom = (n**2)+1
        for i in range(self.n):
            self.union(self.VirtualTop,self.RowCoulmn_index(0,i))
            self.union(self.VirtualBottom,self.RowCoulmn_index(n-1,i))
    def find(self,p):
        if self.blocks[p] != p:
            self.blocks[p] = self.find(self.blocks[p])
        return self.blocks[p]
    def union(self,p,q):
        Rootp = self.find(p)
        Rootq = self.find(q)
        if self.size[Rootq]<self.size[Rootp]:
            self.blocks[Rootq] = self.blocks[Rootp]
            self.size[Rootp] += self.size[Rootq]
        else:
            self.blocks[Rootp] = self.blocks[Rootq]
            self.size[Rootq] += self.size[Rootp]
    def RowCoulmn_index(self,row,coulmn,SideOFIt:str = None):
        if SideOFIt == None:
            return (self.n*row)+coulmn
        elif SideOFIt == 'l':
            if coulmn > 0:
                return self.RowCoulmn_index(row,coulmn-1)
        elif SideOFIt == 'r':
            if coulmn < self.n-1:
                return self.RowCoulmn_index(row,coulmn+1)
        elif SideOFIt == 'u':
            if row >0:
                return self.RowCoulmn_index(row-1,coulmn)
        elif SideOFIt == 'd':
            if row < self.n-1:
                return self.RowCoulmn_index(row+1,coulmn)
        return None      
    def IsOpen(self,row,coulmn,i = None):
        return self.IsOpened[self.RowCoulmn_index(row,coulmn,i)]
    def Open(self,row,coulmn):
        if self.IsOpen(row,coulmn) == False:
            Sides = ['l','r','u','d']
            index = self.RowCoulmn_index(row,coulmn)
            self.IsOpened[index] = True
            self.NoOfOpenSites+=1
            for i in Sides:
                if self.RowCoulmn_index(row,coulmn,i) is not None and self.IsOpen(row,coulmn,i):
                    self.union(index,self.RowCoulmn_index(row,coulmn,i))
    def isFull(self,row,coulmn):
        return self.IsOpen(row,coulmn) and self.find(self.VirtualTop) == self.find(self.RowCoulmn_index(row,coulmn))
    def percolates(self):
        return self.find(self.VirtualTop) == self.find(self.VirtualBottom)