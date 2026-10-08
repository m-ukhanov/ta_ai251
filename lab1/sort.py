def selection_sort(arr):
	comps=0
	assigns=0

	size = len(arr) # Size of an array

	for i in range(size-1):
		min_index = i # Assume the minimal is at index i
		assigns+=1

		for j in range(i+1, size): # Checking the rest of an array
			comps+=1
			if arr[j] < arr[min_index]: # Is arr[min_index] truly the minimal?
				min_index=j
				assigns+=1

		print(f"Step {i}: Minimal is arr[{min_index}]={arr[min_index]}; changed with arr[{i}]={arr[i]}.")

		if min_index != i:
			arr[i], arr[min_index] = arr[min_index], arr[i] # Swap elements if needed
			assigns+=3

		print(f"Comparisons: {comps}; Assignments: {assigns}.")
		
		print(list(el for el in arr),"\n")

def insertion_sort(arr):
	comps=0
	assigns=0

	size = len(arr) # Size of an array

	for j in range(1,size):
		key = arr[j]  # Current element, to insert
		i=j-1 # Previous element

		assigns+=2
		while i>=0 and arr[i]>key: # Move elements greater than key one pos to the right
			comps+=1

			arr[i+1]=arr[i] # Move larger to right
			i-=1 # Move next to left

			assigns+=2

		if i>=0:
			comps+=1

		arr[i+1]=key # Inserting key
		assigns+=1

		print(f"Step {j}: Inserted key = {key}.")
		print(f"Comparisons: {comps}; Assignments: {assigns}.")
		print(list(el for el in arr),"\n")

to_sort = [86, 36, 14, 50, 64, 21, 2, 83, 82]

print(f"Starting array: {list(el for el in to_sort)}")
print("\nSelection sort:")
selection_sort(to_sort.copy())

print("\nInsertion sort:")
insertion_sort(to_sort.copy())
