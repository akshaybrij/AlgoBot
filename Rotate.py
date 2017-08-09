class Rotate:
    def __init__(self):
        pass
    def operation(self,arr):
        n=len(arr)
        for i in range(n-1):
         temp=arr[0]
         for i in range(n-1):
            arr[i]=arr[i+1]
         arr[n-1]=temp;
         return arr
