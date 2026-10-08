comps=0
assigns=0

def swap(arr,i,j):

	global assigns
	arr[i],arr[j]=arr[j],arr[i]
	assigns+=3

def sink(arr, i, n):

	global comps, assigns
	k=i # Index of current
	while True:
		j=2*k+1 # Left index
		print(f"Checking children of arr[{k}] = {arr[k]}")
		if j>=n: # Left exists?
			print(f"No children, sink finished")
			break
		comps+=1
		if j+1 < n and arr[j+1] > arr[j]: # Right exists and bigger than left? 
			print(f"Choosing right child arr[{j}]={arr[j]}")
			j+=1 # Choosing right index
		else:
			print(f"Choosing left child arr[{j}]={arr[j]}")
		comps+=1
		
		print(f"Comparing parent arr[{k}]={arr[k]} >= child arr[{j}]={arr[j]} -> {arr[k] >= arr[j]}")
		if arr[k] >= arr[j]:
			print(f"Parent is in correct position, sink finished")
			break # No need to change if parent is >= biggest child

		print(f"Swapping parent and child")
		swap(arr,k,j) # Swapping child and parent
		print(f"Array after swap: {arr}")
		k=j #Swapping indexes

def heapsort(arr):

	global comps, assigns
	size = len(arr) # Size of an array

	print(f"\nBuilding Max-Heap\n")
	for i in range(size//2-1,-1,-1): # P1: Building Max-Heap
		print(f"Sinking arr[{i}] = {arr[i]}")
		sink(arr,i,size)
	print(f"Array after building heap: {arr}")

	print(f"\nSorting")
	for i in range(size-1,0,-1): #P2: Sorting 
		print(f"\nHeap: {arr[:size]}")
		print(f"Sorted: {arr[size:]}\n")
		print(f"Swapping starting ({arr[0]}) and ending ({arr[i]}) items")
		swap(arr,0,i)

		size-=1 #Deleting sorted item
		print(f"Heap sized down to {size}")
		sink(arr,0,size) #Sinking 
		print(f"Array at step {len(arr)-i}: {arr}")

	return arr

to_sort = [86, 36, 14, 50, 64, 21, 2, 83, 82]

print(f"Starting array: {list(el for el in to_sort)}")
print("Heapsort:")
result1 = heapsort(to_sort.copy())
print(f"Sorted array: {result1}\nComps: {comps}\nAssigns: {assigns}")
