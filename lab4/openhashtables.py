from math import floor
comps=0
assigns=0
collisions=0
A=0.6180339887 #Knuth's constant

sym = list("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")
hash_dict = {letter: i for i, letter in enumerate(sym,1)} #evading exception handling with arrays

words="не той друг хто медом маже а той хто правду каже".lower().split(" ")

def division_method(key,size):
	return key%size

def multiplication_method(key,size):
	return floor(size*((key*A)%1))

def build_open_table(dictionary, size, text, hash_function):
	global comps,assigns,collisions
	hash_table = [[] for x in range(size)] #create table
	assigns+=1

	for word in text:
		print(f"\nInserting word {word}")
		key = sum(dictionary.get(c,0) for c in word)
		assigns+=len(word)+1
		comps+=1

		print(f"Key = {key}")

		address = hash_function(key,size)
		assigns+=1
		print(f"Address = {address}")

		if len(hash_table[address])>0:
			collisions+=1
			for e in hash_table[address]:
				comps+=1

		hash_table[address].append(word)
		assigns+=1 
		print(f"Hash table = {hash_table}")

	return hash_table

def print_table(table):
	print("\n"+"="*65)
	for i in range(len(table)): 
		print(f"Index [{i}]: {table[i]}")
	print("="*65)

def print_comparables():
	global comps,assigns,collisions
	print(f"Average comps: {comps/len(words)}\nAverage assigns: {assigns/len(words)}\nCollisions: {collisions}")
	assigns,comps,collisions=0,0,0

print("Division method (m=13):")
print_table(build_open_table(hash_dict,13,words,division_method))
print_comparables()

print("Multiplication method (m=16):")
print_table(build_open_table(hash_dict,16,words,multiplication_method))
print_comparables()
