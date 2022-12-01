from puzzle_generator import *

fib_seed = [1, 1, 2, 3, 5, 8, 1, 3]

""" 
idea: usually seeds aren't visible at all in the random structures they generate
	  what if they were? what if specific seeds could be used to generate specific aesthetics?
	  
specifically: 	what if i wanted a bunch of puzzles with an even/odd motif? what about a specific sequence of numbers?
	  			would easily extend to a general random generator for puzzles: pick a wide enough "seed space" and draw randomly!
	  			also, enables variation between similar puzzles: use one seed, and pick the two "most different" puzzles, and present them in sequence
"""

# given the base of a mountain climbers puzzle, enumerate all puzzles.
def base_seed(seed):
	size = max(len(seed), max(seed))
	missing = T(size) - sum(seed)
	empty = range(2 * len(seed) - 1, T(size))
	for locations in [list(i) for i in itertools.combinations_with_replacement(empty, missing)]:
		puzzle = seed + [len([i for i in locations if i == j]) for j in range(len(seed), T(size))]
		if count_solutions(get_hex_puzzle(puzzle), size) == 1:
			print(puzzle)	


# given the base AND a list of other acceptable clues, enumerate all puzzles
def base_seed_with_secondary(seed, secondary):
	k = 1
	size = max(len(seed), max(seed))
	empty = range(2 * len(seed) - 1, T(size))
	for locations in [list(i) for i in list(itertools.combinations(empty, len(secondary)))]:
		dic = {locations[i]: secondary[i] for i in range(len(secondary))}
		puzzle = seed + [dic[i] if i in locations else 0 for i in range(8, 36)]
		if count_solutions(get_hex_puzzle(puzzle), size) == 1:
			print(puzzle)	
		k += 1
		if k % 100 == 0: print(k)

base_seed_with_secondary(fib_seed, [1, 1, 2, 3, 5])
#given the tip of a mountain climbers puzzle, enumerate all puzzles (NB: not very functional as of yet, hard to find good seeds here bc of symmetry issues)

pascal_seed = [1, 2, 1, 0, 1, 1, 0, 1, 0, 1]
def top_seed(seed, size):
	missing = T(size) - sum(seed)
	k = 1
	zeros = [0 for i in range(T(size) - len(seed) - inv_T(len(seed)), T(size) - len(seed) + 1)]
	for locations in [list(i) for i in itertools.combinations_with_replacement(range(T(size) - len(seed) - inv_T(len(seed)) - 1), missing)]:
		#print(locations)
		bottom = [len([i for i in locations if i == j]) for j in range(T(size) - len(seed) - inv_T(len(seed)) - 1)]
		#print(bottom)
		if max(bottom) <= size:
			puzzle = bottom + zeros + seed
			if count_solutions(get_hex_puzzle(puzzle), size) == 1:
				print(puzzle)
				print("yahoo")
				exit()	

#top_seed(pascal_seed, 7)