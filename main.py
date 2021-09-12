def medianOfArrays(arr1, arr2):
  arrMax = arr2
  arrMin = arr1
  
  if len(arr1) > len(arr2):
    arrMax = arr1
    arrMin = arr2

  sum = 0

  for i in range(len(arrMax)):
    if i >= len(arrMin):
      sum += arrMax[i]
    else:
      sum += arrMax[i] + arrMin[i]

  print(sum/(len(arrMax)+len(arrMin)))


medianOfArrays([0, 0], [0, 0])