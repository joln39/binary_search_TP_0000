def binary_search(arr,target):
     left = 0
     right = len(arr) - 1

     while left <= right :
         mid = (left + right) // 2
         if arr[mid] == target :
             return mid
         elif arr[mid] > target :
             right = mid - 1
         else:
             left = mid + 1


     return -1


arr = [ 1,3,5,7,9,11,13,15,17,19]
target = 7
result = binary_search(arr, target)

if result != -1 :
    print(f" Element {target} found at index {result}")
else:
    print("Element ont found in the List")
