class Sort:
    def __init__(self):
        pass
    def operation(self,array):
        n=len(array)
        print array
        for i in range(n-1):
            for j in range(n-1):
                if(array[i]>array[j+1]):
                    temp = array[i]
                    array[i]=array[j+1]
                    array[j+1]=temp
        return array
