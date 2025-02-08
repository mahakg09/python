arr=list(map(int, input("Enter array elements separated by space: ").split()))
target=int(input())
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(i,j)
        else:
            print("not found")
            break