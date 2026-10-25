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

def build_closed_table(dictionary, size, text, hash_function):
	global comps,assigns,collisions
	hash_table = [None]*size #create table
	assigns+=1

	for word in text:
		print(f"\nInserting word {word}")
		key = sum(dictionary.get(c,0) for c in word)
		print(f"Key: {key}")
		assigns+=len(word)+1

		address=hash_function(key,size)
		print(f"Entering cycle")
		assigns+=1
		for x in range(size):
			new_address=(address+x)%size
			print(f"Address: {new_address}")
			assigns+=1
			comps+=1
			if hash_table[new_address] is None:
				print(f"Address was None, inserting word.")
				hash_table[new_address]=word
				assigns+=1
				break
			print(f"Collision detected, going for next iteration")
			collisions+=1
		else:
			print(f"Table overflow: omitted {word}")
		print(f"Hash table: {hash_table}")

	return hash_table

def print_table(table):
	print("\n"+"="*65)
	for i in range(len(table)): 
		print(f"Index [{i}]: {table[i]}")
	print("="*65 + "\n")

def print_comparables():
	global comps,assigns,collisions
	print(f"\nAverage comps: {comps/len(words)}\nAverage assigns: {assigns/len(words)}\nCollisions: {collisions}\n")
	assigns,comps,collisions=0,0,0

print("Division method (m=13):")
print_table(build_closed_table(hash_dict,13,words,division_method))
print_comparables()

print("Multiplication method (m=16):")
print_table(build_closed_table(hash_dict,16,words,multiplication_method))
print_comparables()
