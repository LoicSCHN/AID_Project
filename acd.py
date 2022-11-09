import matplotlib.pyplot as plt
import numpy as np

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

def sorter(arr):
# Driver code to test above
    n = len(arr)
    mergeSort(arr, 0, n-1)
    arr = arr[::-1]
    return arr


def grapher(k, l, n): 
    y = k
    z = l
    i = 0
    x = []
    while (i< n):
        x.append(i)
        i += 1
    print(x)
    print(y)
    print(z)
    plt.plot(x, y, label = "students")
    plt.plot(x, z, label = "universities")
    plt.ylabel ("satisfaction")
    plt.xlabel("students/establishment number")
    plt.legend()
    plt.show()
    
   
        

# premier array doit être la satisfaction des étudiants 
# le deuxieme la satisfaction des établissemensts


#arr = [10,9,13,12,8,9,10,5,6,7,8,9,10,9] #example array
#arr2 = [5,8,8,8,8,9,10,3,1,5,10,9,2,5] # example array


grapher(sorter(arr), sorter(arr2), len(arr))