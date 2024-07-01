"""
You are given a function, void MaxInArray(int arr[], int length); The function accepts an integer array ‘arr’ of size ‘length’ as its argument. Implement the function to find the maximum element of the array and print the maximum element and its index to the standard output """

arr=list(map(int,input().split()))
max=arr[0]
for i in range(len(arr)):
    if(arr[i]>=max):
        max=arr[i]
        maxindex=i
print(arr[i])
print(maxindex)