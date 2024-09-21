from protogen import run_file # Bytogen acts as no more than a compiler from Bytogen to Protogen

file_extension = ".bytogen"

# if byte == 0x41: protogen_code += b'A'
# elif byte == 0x42: protogen_code += b'B'
# elif byte == 0x61: protogen_code += b'a'
# elif byte == 0x62: protogen_code += b'b'
# elif byte == 0x63: protogen_code += b'c'
# elif byte == 0x65: protogen_code += b'e'
# elif byte == 0x2b: protogen_code += b'+'
# elif byte == 0x2d: protogen_code += b'-'
# elif byte == 0x2b: protogen_code += b'&'
# elif byte == 0x7c: protogen_code += b'|'
# elif byte == 0x5e: protogen_code += b'^'
# elif byte == 0x6a: protogen_code += b'j'
# elif byte == 0x3e: protogen_code += b'>'
# elif byte == 0x3d: protogen_code += b'='
# elif byte == 0x3c: protogen_code += b'<'
# elif byte == 0x72: protogen_code += b'r'
# elif byte == 0x00: protogen_code += b'N'
# elif byte == 0x2C: protogen_code += b','
# elif byte == 0x2E: protogen_code += b'.'
# elif byte == 0x3B: protogen_code += b';'
# elif byte == 0x3A: protogen_code += b':'
# elif byte == 0x3F: protogen_code += b'?'

def convert_bytogen_to_protogen(file_path):
	with open(file_path, 'rb') as file:
		src_code = file.read()

	protogen_code = b''
	for byte in src_code:
		if byte == ord('A'): protogen_code += 0x41
		elif byte == ord('B'): protogen_code += 0x42
		elif byte == ord('a'): protogen_code += 0x61
		elif byte == ord('b'): protogen_code += b'b'
		elif byte == ord('c'): protogen_code += b'c'
		elif byte == ord('e'): protogen_code += b'e'
		elif byte == ord('+'): protogen_code += b'+'
		elif byte == ord('-'): protogen_code += b'-'
		elif byte == ord('&'): protogen_code += b'&'
		elif byte == ord('|'): protogen_code += b'|'
		elif byte == ord('^'): protogen_code += b'^'
		elif byte == ord('j'): protogen_code += b'j'
		elif byte == ord('>'): protogen_code += b'>'
		elif byte == ord('='): protogen_code += b'='
		elif byte == ord('<'): protogen_code += b'<'
		elif byte == ord('r'): protogen_code += b'r'
		elif byte == ord('N'): protogen_code += b'N'
		elif byte == ord(','): protogen_code += b','
		elif byte == ord('.'): protogen_code += b'.'
		elif byte == ord(';'): protogen_code += b';'
		elif byte == ord(':'): protogen_code += b':'
		elif byte == ord('?'): protogen_code += b'?'

	with open(file_path + file_extension, 'wb') as file:
		file.write(protogen_code)
