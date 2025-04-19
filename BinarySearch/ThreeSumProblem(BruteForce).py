def ThreeSum(l:list):
    count = 0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            for k in range(j+1, len(l)):
                print(l[i],"+",l[j],"+",l[k] ,"=",l[i]+l[j]+l[k])
                if l[i]+l[j]+l[k] == 0:
                    count +=1
    return count
ThreeSum([1,-2,1,5,-3,-2])