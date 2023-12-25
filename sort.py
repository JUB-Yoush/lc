class Sort():
	def __init__(self) -> None:
		pass
	def binsearch(arr,target):
		l = 0
		r = len(arr) -1
		while l <= r:
			m = (l+r) //2
			if arr[m] == target:
				return f"target {target} located at index {m}"
			if arr[m] > target:
				r = m -1
			if arr[m] < target:
				l = m +1
		return f"target {target} not present in list."
	'''
	loop from 1 not from 0 (one value is always sorted)
	check if j (i+1) is > i
	if not then swap them
	'''		

	def insertion(arr):
		for i in range(1,len(arr)):
			val = arr[i]
			j = i -1
			while j >= 0 and val < arr[j]:
				arr[j+1] = arr[j]
				j -= 1
			arr[j+1] = val
		return arr

	'''	
	split into halves until one value
	then combine halves together.
	use pointers within the original array to keep size constant-ish
	'''
	def mergeSort(arr):
		def merge(left,right):
			output = []
			i = j = 0
			while i < len(left) and j < len(right):
				if left[i] < right[j]:
					output.append(left[i])
					i += 1
				else:
					output.append(right[j])
					j += 1
			output.extend(left[i:])
			output.extend(right[j:])

		if len(arr) == 1: return arr
		mid = len(arr) //2
		left = self.mergeSort(list[:mid])
		right = self.mergeSort(list[mid:])
		return merge(left,right)

				

print(Sort.mergeSort([3,2,4,1,6]))