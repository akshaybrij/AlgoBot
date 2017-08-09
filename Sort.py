class Sort:
    def __init__(self):
        pass
    def operation(self,array):
        n=len(array)
        for i in range(n-1):
            for j in range(n-1):
                if(array[j]>array[j+1]):
                    temp = array[j]
                    array[j]=array[j+1]
                    array[j+1]=temp
        return array
