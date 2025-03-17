from PercolationDataStructure import Percolation as p
import random as r
import numpy as np
class PercolationSimulation:
    def __init__(self,trials,WorldSize):
        self.trials = trials
        self.WorldSize = WorldSize
        self.trials = trials
        self.result = []
        
    def RunSimulation(self):
        for _ in range(self.trials):
            self.PercolationWorld = p(self.WorldSize)
            self.OpenedSites = 0
            OpenedPositions = set()
            while self.PercolationWorld.percolates() == False:
                row = r.randint(0,self.WorldSize-1)
                colmn = r.randint(0,self.WorldSize-1)
                if (row,colmn) not in OpenedPositions:
                    self.PercolationWorld.Open(row,colmn)
                    OpenedPositions.add((row,colmn))
                    self.OpenedSites+=1
            self.result.append(self.OpenedSites/(self.WorldSize**2))
    def mean(self):
        return np.mean(self.result)
    def stddev(self):
        return np.std(self.result,ddof=1)
    def confidenceLo(self):
        return self.mean()-(1.96 *self.stddev() / np.sqrt(len(self.result)))
    def confidenceHi(self):
        return self.mean()+(1.96 *self.stddev() / np.sqrt(len(self.result)))
