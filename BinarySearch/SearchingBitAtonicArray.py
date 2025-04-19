class SearchingBitAtonicArray:
    def __init__(self,arr:list[int],num:int):
        self.arr = arr
        self.num = num
        self.PeekIndex = self.Peek(0,len(arr)-1)
        self.NumIndex = self.BSincreasingPart(0,self.PeekIndex)
        if self.NumIndex == -1:
            self.NumIndex = self.BSdecreaseingPart(self.PeekIndex,len(self.arr)-1)
            if self.NumIndex == None:
                print("This num isn't here")
    def Peek(self,low,high):
        if high == low:
            return high
        mid = (low+high)//2
        if self.arr[mid] < self.arr[mid + 1]:
            return self.Peek(mid+1,high)
        elif self.arr[mid] > self.arr[mid + 1]:
            return self.Peek(low,mid)
    def BSincreasingPart(self,low,high):
        mid = (low + high)//2
        if low > high:
            return -1
        if self.arr[mid] == self.num:
            return mid
        elif self.arr[mid] > self.num:
            return self.BSincreasingPart(low,mid-1)
        elif self.arr[mid] < self.num:
            return self.BSincreasingPart(mid+1,high)
    def BSdecreaseingPart(self,high,low):
        mid = (high + low)//2
        if high > low:
            return None
        if self.arr[mid] == self.num:
            return mid
        elif self.arr[mid] < self.num:
            return self.BSdecreaseingPart(high,mid -1)
        elif self.arr[mid] > self.num:
            return self.BSdecreaseingPart(mid+1,low)
        


arr = [3, 22, 34, 40, 52, 84, 112, 137, 156, 168, 170, 178, 183, 217, 229, 231, 275, 325, 329, 335, 343, 355, 368, 371, 383, 394, 426, 427, 433, 437, 439, 442, 445, 464, 515, 526, 544, 550, 553, 559, 568, 574, 585, 590, 597, 615, 633, 638, 701, 704, 728, 730, 734, 742, 807, 808, 830, 852, 854, 860, 905, 947, 959, 974, 961, 955, 942, 902, 895, 881, 868, 863, 860, 827, 824, 801, 735, 695, 663, 604, 571, 555, 510, 382, 319, 279, 276, 224, 217, 200, 149, 92, 70, 48, 45, 37, 36, 31, 17, 14]   
a = SearchingBitAtonicArray(arr,852).NumIndex
print(a)
print(arr[a])