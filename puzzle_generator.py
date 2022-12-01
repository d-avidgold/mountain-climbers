"""
https://tinyurl.com/2ekrgurx for first three puzzles
https://tinyurl.com/2qvqe6m9 for final large puzzle
"""

from brute_force_solver import *

def get_hex_puzzle(upClues):
	height = inv_T(len(upClues))
	return({"up": upClues, "down": [0 for i in range(T(height - 1))]})


if __name__ == "__main__":
	# BINARY PUZZLE:
	for bottom_row_ones in [list(i) for i in list(itertools.combinations([0,1,2,3,4], 3))]:
		for second_row_twos in [list(i) for i in list(itertools.combinations([0, 1,2,3], 2))]:
			bottom_row = [1 if i in bottom_row_ones else 0 for i in range(5)]
			second_row = [2 if i in second_row_twos else 0 for i in range(4)]
			upClues = bottom_row + second_row + [0, 0, 0, 4, 4, 0]
			if count_solutions(get_hex_puzzle(upClues), 5) == 1:
				print(upClues)
	
	# TERNARY PUZZLE:
	for bottom_row_ones in [list(i) for i in list(itertools.combinations([0,1,2,3], 2))]:
		for second_row_ones in [list(i) for i in list(itertools.combinations([0,1,2], 2))]:
			bottom_row = [1 if i in bottom_row_ones else 0 for i in range(4)]
			second_row = [1 if i in second_row_ones else 0 for i in range(3)]
			upClues = bottom_row + second_row + [3, 3, 0]
			#print(count_solutions(get_hex_puzzle(upClues), 4))
			if count_solutions(get_hex_puzzle(upClues), 4) == 1:
				print(upClues)
	
	# PI PUZZLE
	for locations in [list(i) for i in list(itertools.combinations([0, 1, 2, 3, 7, 8, 9], 2))]:
		upClues = [1 if (i in locations) else 0 for i in range(4)] + [3, 1, 4] + [1 if (i in locations) else 0 for i in range(7, 10)]
		if count_solutions(get_hex_puzzle(upClues), 4) == 1:
			print(upClues)
	
	for location in [0, 1, 2, 3, 7, 8, 9]:
		upClues = [2 if (i == location) else 0 for i in range(3)] + [3, 1, 4] + [2 if (i == locations) else 0 for i in range(7, 10)]
		if count_solutions(get_hex_puzzle(upClues), 4) == 1:
			print(upClues)
	
	# FIBONACCI PUZZLE, reimplemented in puzz_gen_from_seed
	for locations in [list(i) for i in list(itertools.combinations(range(15, 26), 5))]:
		dic = {locations[0]: 1, locations[1]: 1, locations[2]: 2, locations[3]: 3, locations[4]: 5}
		upClues = [1, 1, 2, 3, 5, 8, 1, 3] + [dic[i] if i in locations else 0 for i in range(8, 36)]
		if count_solutions(get_hex_puzzle(upClues), 8) == 1:
			print(upClues)