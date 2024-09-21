import os
import sys
import random

debug = False

def bytes_to_int (b) : # Turns the bytes to an int with the bytes in the correct order
	return bytes_to_int_reverse_order(b[::-1])

def bytes_to_int_reverse_order (b) : # Turns the bytes to an int, but with the bytes reversed
	return sum([num*256**scale for num, scale in zip(b, range(len(b)))])

WIDTH = 4 # Replaced with 2**(the first byte of the file)
		# The first WIDTH bytes are removed, encluding the one used.
		# Row 0 is for formatting stuff.

def run_file(file_path) :
	global WIDTH, depth_stack, regesters, character_input_que

	WIDTH = 4 # Replaced with 2**(the first byte of the file)
	depth_stack = []
	regesters = {'A':0,'B':0,'C':0,'E':0}
	character_input_que = ''

	src_code = b''

	with open(file_path, 'rb') as file :
		src_code = file.read()
		WIDTH = 2 ** src_code[0] # Set the WIDTH to 2**(first byte) [0x02 -> 4 and 0x08 -> 256]
		# src_code = src_code[WIDTH:] # Throw out the top row -- changed my mind, let's leave it

	current_line_position = WIDTH
	depth_stack.append(current_line_position)

	while len(depth_stack) > 0 :
		current_line_position = depth_stack.pop()
		while True :
			current_line = src_code[current_line_position:current_line_position+WIDTH-current_line_position%WIDTH]
			match current_line[0]:
				case 65: #A # Set regester A to value
					regesters['A'] = current_line[1]
					if debug:
						print(f"A = {regesters['A']}")
				case 66: #B # Set regester B to value
					regesters['B'] = current_line[1]
					if debug:
						print(f"B = {regesters['B']}")
				case 97: #a # Set regester A to value of a byte at the provided location
					regesters['A'] = src_code[bytes_to_int_reverse_order(current_line[1:])]
					if debug:
						print(f"A = {regesters['A']}")
				case 98: #b # Set regester B to value of a byte at the provided location
					regesters['B'] = src_code[bytes_to_int_reverse_order(current_line[1:])]
					if debug:
						print(f"B = {regesters['B']}")
				case 99: #c # Set the value of the byte location provided to the C regester's value
					location = bytes_to_int_reverse_order(current_line[1:])
					src_code = src_code[:location]+int.to_bytes(regesters['C'], length = 1, byteorder = 'little')+src_code[location+1:]
					if debug:
						print(f"Set byte at {location} to {regesters['C']}")
				case 101: #e # Set the value of the byte location provided to the E regester's value
					location = bytes_to_int_reverse_order(current_line[1:])
					src_code = src_code[:location]+int.to_bytes(regesters['E'], length = 1, byteorder = 'little')+src_code[location+1:]
					if debug:
						print(f"Set byte at {location} to {regesters['E']}")
				# I'll use brackets to mean [_] = Regester _ in the comments to not type as much from here on out...
				case 43: #+ # [A] + [B] = [C] ([E] = 1 for overflow, and 0 otherwise)
					regesters['C'] = regesters['A'] + regesters['B']
					regesters['E'] = 0
					while regesters['C'] > 255 :
						regesters['C'] -= 256
						regesters['E'] += 1
					if debug:
						print(f"A + B = {regesters['C']}")
				case 45: #- # [A] - [B] = [C] ([E] = 255 for underflow, and 0 otherwise)
					regesters['C'] = regesters['A'] - regesters['B']
					regesters['E'] = 0
					while regesters['C'] < 0 :
						regesters['C'] += 256
						regesters['E'] -= 1
					while regesters['E'] < 0 :
						regesters['E'] += 256
					if debug:
						print(f"A - B = {regesters['C']}")
				case 38: #& # [A] & [B] = [C] ([E] = 0)
					regesters['C'] = regesters['A'] & regesters['B']
					regesters['E'] = 0
					if debug:
						print(f"A & B = {regesters['C']}")
				case 124: #| # [A] | [B] = [C] ([E] = 0)
					regesters['C'] = regesters['A'] | regesters['B']
					regesters['E'] = 0
					if debug:
						print(f"A | B = {regesters['C']}")
				case 94: #^ # [A] ^ [B] = [C] ([E] = 0)
					regesters['C'] = regesters['A'] ^ regesters['B']
					regesters['E'] = 0
					if debug:
						print(f"A ^ B = {regesters['C']}")
				case 106: #j # Jump to the address
					current_line_position = bytes_to_int_reverse_order(current_line[1:]) - WIDTH
					if debug:
						print(f"Jumping to {current_line_position}")
				case 62: #> # Jump to the address if [A] > [B]
					if regesters['A'] > regesters['B'] :
						current_line_position = bytes_to_int_reverse_order(current_line[1:]) - WIDTH
						if debug:
							print(f"Jumping to {current_line_position}")
				case 61: #= # Jump to the address if [A] == [B]
					if regesters['A'] == regesters['B'] :
						current_line_position = bytes_to_int_reverse_order(current_line[1:]) - WIDTH
						if debug:
							print(f"Jumping to {current_line_position}")
				case 60: #< # Jump to the address if [A] < [B]
					if regesters['A'] < regesters['B'] :
						current_line_position = bytes_to_int_reverse_order(current_line[1:]) - WIDTH
						if debug:
							print(f"Jumping to {current_line_position}")
				case 114: #r # Jump to the address and return to the next line later
					depth_stack.append(current_line_position+WIDTH)
					current_line_position = bytes_to_int_reverse_order(current_line[1:]) - WIDTH
					if debug:
						print(f"Returning to {current_line_position+WIDTH}")
				case 44: #, # Input char (Like BrainF***) (Store in [C])
					if len(character_input_que) == 0 :
						character_input_que += input()
					if len(character_input_que) == 0 :
						regesters['E'] = 1
						regesters['C'] = 0
					else :
						regesters['E'] = 1 if len(character_input_que)==1 else 0 # [E] is one for end of input
						regesters['C'] = ord(character_input_que[0])
						character_input_que = character_input_que[1:]
					if debug:
						print(f"Input char: {regesters['C']}")
				case 59: #; # Input unsigned 8-bit int (Store in [C])
					character_input_que = ''
					i = int(input())
					regesters['C'] = i%256
					regesters['E'] = 0 if i == regesters['C'] else 1
					if debug:
						print(f"Input int: {regesters['C']}")
				case 46: #. # Output char (Like BrainF***) (Get from [A])
					print(chr(regesters['A']), end='')
					if debug:
						print(f"Outputting {regesters['A']}")
				case 58: #: # Output unsigned 8-bit int (Get from [A])
					print(regesters['A'], end='')
					if debug:
						print(f"Outputting {regesters['A']}")
				case 63: #? # Set [C] to a random number between [A] and [B] inclusive
					regesters['C'] = random.randint(regesters['A'], regesters['B'])
					if debug:
						print(f"Set C to {regesters['C']}")
				case 0: #Nothing # Go back to the last thing in the depth_stack and pop that bad boi
					break # Do this via breaking out of the while True
				case _:
					# This should not occur. I'll treat it like a comment, I guess.
					pass
			current_line_position += WIDTH

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

def main():
	try:
		cls()
		global debug
		debug = input("Debug mode? [NOTE: Debug mode results in significantly longer and harder to read terminal space for a minimal amount of debugging tools. It's only provided for sake of fun.] (y/n): ").lower() == 'y'
		cls()
		# if no file is specified, ask the user what example program they would like to run
		if len(sys.argv) == 1:
			examples = os.listdir('examples')
			print("Which example would you like to run?")
			for i, name in enumerate(examples):
				print(f"{i+1}. {name}")
			choice = int(input("Enter the number: "))

			cls()

			run_file(f"examples/{examples[choice-1]}")
		else:
			cls()
			run_file(sys.argv[1])
	except KeyboardInterrupt:
			cls()

if __name__ == "__main__":
	main()