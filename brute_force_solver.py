import itertools
import math

puzzle = {"up": [1, 0, 3, 0, 1, 0, 2, 2, 0, 1], "down": [0, 0, 0, 0, 0, 0]}
puzzle2 = {"up": [1, 2, 3, 0, 0, 0], "down": [0, 0, 0]}
puzzle3 = {"up": [1, 0, 2, 0, 0, 0], "down": [2, 1, 0]}
impossiblePuzzle = {"up": [1, 0, 3, 0, 0, 0], "down": [2, 1, 0]}
# given a solution (a permutation of N digits), get the directions (up, left, right) for each climber
def get_directions(solution):

	if solution == []:
		return({})

	directions = {}

	restOfPuzzle = [i - 1 for i in solution if i != 1]
	restOfPuzzleDirections = get_directions(restOfPuzzle)
	seenOne = False
	for i in range(0, len(solution)):
		climber = solution[i]
		if climber == 1:
			seenOne = True
			directions[climber] = ""
		else:
			if seenOne:
				directions[climber] = "LU" + restOfPuzzleDirections[climber - 1]
			else:
				directions[climber] = "RU" + restOfPuzzleDirections[climber - 1]
	#print(directions)
	return(directions)

# get n^th triangular number
def T(n):
	if n >= 0:
		return(int(n * (n + 1) / 2))
	else:
		return(0)

def inv_T(m):
	return(int(math.sqrt(2 * m + 1/ 4) - 1/2))

# given a solution (a permutation of N digits), get the indices of spots visited (up triangle, down triangle, etc.) for each climber
def get_relative_paths(solution):
	directions = get_directions(solution)
	relative_coords = {}
	k = 1
	for i in solution:
		path_coords = [k]
		direct = directions[i]
		for j in direct:
			if j == "U" or j == "R": path_coords.append(path_coords[-1])
			if j == "L": path_coords.append(path_coords[-1] - 1)
		relative_coords[i] = path_coords
		k += 1
	return(relative_coords)

# converts relative indices to actual coordinates
def convert_relative_to_actual(path, n):
	actual_coords = []
	for i in range(len(path)):
		if i % 2 == 0:
			rowNum = i / 2
			actual_coords.append(path[i] + T(n) - T(n - rowNum))
		else:
			rowNum = (i - 1) / 2
			actual_coords.append(path[i] + T(n - 1) - T(n - 1 - rowNum))
	return(actual_coords)

def get_paths(solution):
	paths = {}
	relative_paths = get_relative_paths(solution)
	for i in solution:
		paths[i] = convert_relative_to_actual(relative_paths[i], len(solution))
	return(paths)

def get_sum_on_path(puzzle, path, expected):
	total = 0
	for i in range(len(path)):
		if i % 2 == 0:
			total += puzzle["up"][path[i] - 1]
		else:
			total += puzzle["down"][path[i] - 1]
		if total > expected:
			return(expected + 1)
	return(total)

def check_solution(puzzle, solution):
	paths = get_paths(solution)
	#print(paths)
	for i in range(1, len(solution) + 1):
		path = paths[i]
		path_sum = get_sum_on_path(puzzle, path, i)
		if path_sum != i:
			return(False)
	return(True)

# brute force checks all solutions. definitely not scalable. at least has some built in safeguards for early short-circuiting, but still incredibly slow.
def count_solutions(puzzle, size):
	tot = 0
	bottom_row = puzzle["up"][0:size]
	for solution in [list(j) for j in list(itertools.permutations(range(1, size + 1)))]:
		keepgoing = True
		for i in range(size):
			if solution[i] < bottom_row[i]:
				keepgoing = False
				break
		if keepgoing and check_solution(puzzle, solution):
			tot += 1
	return(tot)

def print_all_solutions(puzzle, size):
	bottom_row = puzzle["up"][0:size]
	for solution in [list(j) for j in list(itertools.permutations(range(1, size + 1)))]:
		keepgoing = True
		for i in range(size):
			if solution[i] < bottom_row[i]:
				keepgoing = False
				break
		if keepgoing and check_solution(puzzle, solution):
			print(solution)
	return()


def get_hex_puzzle(upClues):

	height = inv_T(len(upClues))
	return({"up": upClues, "down": [0 for i in range(T(height - 1))]})

fib_puzzle = get_hex_puzzle([1, 1, 2, 3, 5, 8, 1, 3, 1, 1, 2, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#print(len([1, 1, 2, 3, 5, 8, 1, 3, 1, 1, 2, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
#print(len(fib_puzzle["up"]))
#print(len(fib_puzzle["down"]))

#print_all_solutions(fib_puzzle, 8)