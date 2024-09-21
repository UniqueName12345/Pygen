file_extension = ".bytogen"

def convert_protogen_to_bytogen(file_path):
	with open(file_path, 'rb') as file:
		src_code = file.read()

	bytogen_code = b''
	for byte in src_code:
		if byte == 0x41: bytogen_code += b'A'
		elif byte == 0x42: bytogen_code += b'B'
		elif byte == 0x61: bytogen_code += b'a'
		elif byte == 0x62: bytogen_code += b'b'
		elif byte == 0x63: bytogen_code += b'c'
		elif byte == 0x65: bytogen_code += b'e'
		elif byte == 0x2b: bytogen_code += b'+'
		elif byte == 0x2d: bytogen_code += b'-'
		elif byte == 0x2b: bytogen_code += b'&'
		elif byte == 0x7c: bytogen_code += b'|'
		elif byte == 0x5e: bytogen_code += b'^'
		elif byte == 0x6a: bytogen_code += b'j'
		elif byte == 0x3e: bytogen_code += b'>'
		elif byte == 0x3d: bytogen_code += b'='
		elif byte == 0x3c: bytogen_code += b'<'
		elif byte == 0x72: bytogen_code += b'r'
		elif byte == 0x00: bytogen_code += b'N'
		elif byte == 0x2C: bytogen_code += b','
		elif byte == 0x2E: bytogen_code += b'.'
		elif byte == 0x3B: bytogen_code += b';'
		elif byte == 0x3A: bytogen_code += b':'
		elif byte == 0x3F: bytogen_code += b'?'

	with open(file_path + file_extension, 'wb') as file:
		file.write(bytogen_code)

if __name__ == '__main__':
	import os
	import shutil

	if not os.path.exists('bytogen_examples'):
		os.mkdir('bytogen_examples')
		for file in os.listdir('protogen_examples'):
			if file.endswith('.protogen'):
				convert_protogen_to_bytogen(os.path.join('protogen_examples', file))
				shutil.move(os.path.join('protogen_examples', file + file_extension), os.path.join('bytogen_examples', file + file_extension))
