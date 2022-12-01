import itertools

"""
    6
  4   5
1 	2 	3

  5
 3 4
0 1 2
"""
def bottom_row_check(n, puzzle):
	for i in puzzle:
		if i <= n: return(True)
	return(False)

def max_flower_check(n, puzzle):
	nHexes = int(n * (n + 1) / 2)
	for hexagon in range(1, nHexes + 1):
		if len([i for i in puzzle if i == hexagon]) > n:
			return(False)
	return(True)

def ensure_summetry(n, puzzle):
	nHexes = int(n * (n + 1) / 2)
	puzzle_dict = {i: len([j for j in puzzle if j == i]) for i in range(1, nHexes + 1)}
	if puzzle_dict[4] < puzzle_dict[5]:
		return(False)
	if puzzle_dict[4] == puzzle_dict[5]:
		if puzzle_dict[1] < puzzle_dict[3]: return(False)
	return(True)

def enumerate_puzzles(n):
	nHexes = int(n * (n + 1) / 2)
	#print(nHexes)
	puzzleList = []

	for puzzle in list(itertools.combinations_with_replacement(range(1, nHexes + 1), nHexes)):
		if bottom_row_check(n, puzzle) and max_flower_check(n, puzzle) and len(set(puzzle)) >= n and ensure_summetry(n, puzzle):
			puzzleList.append(puzzle)
			# print(str(puzzle) + " valid")
		# else:
			# print(str(puzzle) + " invalid")
	return(puzzleList)

def print_puzzle(puzzle, n):
	nHexes = int(n * (n+1) / 2)
	puzzle_dict = {i: len([j for j in puzzle if j == i]) for i in range(1, nHexes + 1)}

	counter = nHexes

	for i in range(1, n + 1):
		s = ""
		for j in range(i):
			if puzzle_dict[counter] == 0: s += "." + " "
			else: s += str(puzzle_dict[counter]) + " "
			counter -= 1
		print(" " * (n - i) + s[::-1])

	return()

puzzles = enumerate_puzzles(3)

p_counter = 0 
print(str(len(puzzles)) + " puzzles found!")
for i in puzzles:
	if p_counter <= 20: 
		print(i)
		print_puzzle(i, 3)
		p_counter += 1
		print()