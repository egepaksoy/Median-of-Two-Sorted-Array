def medianOfArrays(arr1, arr2):
  arr = arr1 + arr2
  arr.sort()

  if len(arr)%2 != 0:
    median = arr[len(arr)//2]
  
  else:
    median = (arr[len(arr)//2-1] + arr[len(arr)//2]) / 2

  return median

print(medianOfArrays([1,3], [2, 7]))