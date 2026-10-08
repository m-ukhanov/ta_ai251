def merge_sort_iter(arr):
	comps=0
	assigns=0

	size = len(arr) # Size of an array
	i=1 # Current size of subarrays

	while i<size:
		j=0
		while j<size-i:
			left=j
			mid=j+i
			right=min(j+2*i,size) #Using min to prevent falling out
			c, a_count = merge(arr,left,mid,right) #Merging the subarrays 
			print("\n")
			comps+=c
			assigns+=a_count
			j+=2*i #Next subarray
		i*=2 #Next subarray size
	return arr, comps, assigns

def merge(arr,left,mid,right):
	comps=0
	assigns=0

	n1=mid-left #Items in left
	n2=right-mid #Items in right
	L=arr[left:mid]
	R=arr[mid:right]

	print(f"Merging arrays: arr[{left}:{mid}] = {L} and arr[{mid}:{right}] = {R}")

	assigns+=n1+n2
	it1=0 #Index of current in L
	it2=0 #Index of current in R
	k=left #Index of replaced item
	assigns+=3
	while it1<n1 and it2<n2:
		comps+=1

		print(f"Comparing {L[it1]} < {R[it2]} -> {L[it1]<R[it2]}")

		if L[it1] < R[it2]: #Merging the left
			print(f"Copying {L[it1]} from L to arr[{k}], replacing {arr[k]}")
			arr[k] = L[it1]
			it1 += 1
			assigns += 1
		else: #Merging the right
			print(f"Copying {R[it2]} from R to arr[{k}], replacing {arr[k]}")
			arr[k] = R[it2] 
			it2 += 1
			assigns +=1
		k +=1
		assigns +=1

	while it1<n1: #Merging remaining left
		print(f"Copying remaining {L[it1]} from L to arr[{k}], replacing {arr[k]}")
		arr[k] = L[it1]
		it1 += 1
		k += 1
		assigns += 1

	while it2<n2: #Merging remaining right
		print(f"Copying remaining {R[it2]} from L to arr[{k}], replacing {arr[k]}")
		arr[k] = R[it2]
		it2 += 1
		k += 1
		assigns += 1

	print(f"Array after merge: {arr}")

	return comps, assigns

def merge_sort_recursive(arr):
	comps=0
	assigns=0
	rec_calls=0

	size=len(arr) # Size of an array

	if size<=1: #Array of 1 is already sorted
		print(f"Reached base case: {arr}")
		return arr,comps,assigns,rec_calls

	mid = size//2
	assigns+=1

	print(f"Splitting {arr}")
	print(f"Left: {arr[:mid]}")
	print(f"Right: {arr[mid:]}")

	rec_calls+=2
	left,c1,a1,r1 = merge_sort_recursive(arr[:mid]) #Sorting recursively left
	right,c2,a2,r2 = merge_sort_recursive(arr[mid:]) #Sorting recursively right
	comps+=c1+c2
	assigns+=a1+a2
	rec_calls+=r1+r2

	print(f"Merging {left} and {right}")

	merged_arr, c_merge, a_merge = merge_rec(left,right) #Merging sorted arrays
	comps+=c_merge
	assigns+=a_merge

	print(f"Array after merge: {merged_arr}")

	print("\n")

	return merged_arr, comps, assigns, rec_calls

def merge_rec(left, right):
	merged_arr=[]
	comps=0
	assigns=0
	i=0 #Index in left
	j=0 #Index in right

	while i<len(left) and j<len(right):
		comps+=1

		print(f"Comparing {left[i]} <= {right[j]} -> {left[i]<=right[j]}")

		if left[i]<=right[j]: #Merging the left
			print(f"Writing {left[i]} from left array")
			merged_arr.append(left[i])
			i+=1
			assigns+=1
		else: #Merging the right
			merged_arr.append(right[j])
			print(f"Writing {right[j]} from right array")
			j+=1
			assigns+=1

	while i<len(left): #Merging remaining left
		print(f"Copying remaining {left[i]} from left array")
		merged_arr.append(left[i])
		i+=1
		assigns+=1
	while j<len(right): #Merging remaining right
		print(f"Copying remaining {right[j]} from right array")
		merged_arr.append(right[j])
		j+=1
		assigns+=1
	return merged_arr, comps, assigns

def quick_sort(arr,l,r):
	comps=0
	assigns=0
	rec_calls=1

	size = len(arr) # Size of an array
	if l<r:
		print(f"Sorting arr[{l}:{r+1}]={arr[l:r+1]}")

		q,c1,a1=partition(arr,l,r)
		comps+=c1
		assigns+=a1

		print(f"Partition finished: q={q}")
		print(f"Left: {arr[l:q+1]}")
		print(f"Right: {arr[q+1:r+1]}\n")

		c2,a2,r2=quick_sort(arr,l,q)
		c3,a3,r3 = quick_sort(arr,q+1,r)
		comps+=c3+c2
		assigns+=a2+a3
		rec_calls+=r2+r3

		print(f"After sorting [{l}:{r}]: {arr[l:r+1]}")

	else:
		print(f"Base case reached: arr[{l}:{r+1}]={arr[l:r+1]}")
		return 0,0,0
	return comps,assigns,rec_calls

def partition(arr,l,r):
	comps=0
	assigns=0
	rec_calls=1

	size = len(arr) # Size of an array

	pivot = arr[l]
	assigns+=1

	print(f"Pivot: arr[{l}]={pivot}")

	i=l-1
	j=r+1
	assigns+=2

	while True:
		i+=1
		assigns+=1
		print("Moving i from left")
		while arr[i]<pivot:
			print(f"Comparing arr[{i}]={arr[i]}<pivot={pivot} -> {arr[i]<pivot}")
			comps+=1
			i+=1
			assigns+=1
		comps+=1
		print(f"Comparing arr[{i}]={arr[i]}<pivot={pivot} -> {arr[i]<pivot}")
		print(f"I stopped at index {i}: arr[{i}]={arr[i]}")

		j-=1
		assigns+=1
		print("Moving j from right")
		while arr[j]>pivot:
			print(f"Comparing arr[{j}]={arr[j]}>pivot={pivot} -> {arr[j]>pivot}")
			comps+=1
			j-=1
			assigns+=1
		comps+=2
		print(f"Comparing arr[{j}]={arr[j]}>pivot={pivot} -> {arr[j]>pivot}")
		print(f"J stopped at index {j}: arr[{j}]={arr[j]}")

		if i>=j:
			print(f"Pointers crossed at index {j}")
			print(f"Array after partition: {arr}")
			return j,comps,assigns

		print(f"Swap: arr[{i}]={arr[i]} <> arr[{j}]={arr[j]}")
		arr[i],arr[j] = arr[j], arr[i]
		assigns+=3
		print(f"Array after swap: {arr}")

to_sort = [86, 36, 14, 50, 64, 21, 2, 83, 82]

print(f"Starting array: {list(el for el in to_sort)}")
print("Iterative merge sort:")
result1 = merge_sort_iter(to_sort.copy())
print(f"Sorted array: {result1[0]}\nComps: {result1[1]}\nAssigns: {result1[2]}")

print(f"\nStarting array: {list(el for el in to_sort)}")
print("Recursive merge sort:")
result2 = merge_sort_recursive(to_sort.copy())
print(f"Sorted array: {result2[0]}\nComps: {result2[1]}\nAssigns: {result2[2]}\nRecursive calls: {result2[3]+1}")

print(f"Starting array: {list(el for el in to_sort)}")
print("Quicksort:")
array=to_sort.copy()
result3 = quick_sort(array,0,len(to_sort)-1)
print(f"Sorted array: {array}\nComps: {result3[0]}\nAssigns: {result3[1]}\nRecursive calls: {result3[2]}")
