class Sorting:
    def insertionSort(list):
        for i in range(1,len(list)):
            j=i
            while j > 0 and list[j-1]>list[j]:
                list[j],list[j-1] = list[j-1],list[j]
                j=j-1
        return list

    def mergeSort(list):
        length = len(list)

        # base case: array is single item
        if length == 1:
            return list

        #split in half and recursively call
        mid = length // 2

        left = mergeSort(list[:mid])
        right = mergeSort(list[mid:])

        # take the two returned lists and stitch them back together
        return merge(left, right)

        def merge(left, right):
            output = []
            i = j = 0

            # loop through each array and pick the lowest value at each point
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    output.append(left[i])
                    i += 1
                else:
                    output.append(right[j])
                    j += 1

            output.extend(left[i:])
            output.extend(left[j:])

            return output






