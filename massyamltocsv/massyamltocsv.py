import sys
import yaml
import os

def getcsv(argv):
	if len(argv) == 0:
		print("No input files given.")
	else:
		flag = True
		out_string = ''
		keys = ['L1c', 'L1b', 'L1a', 'L2c', 'L2b', 'L2a', 'L2prf',
				'TLBe', 'TLBp', 'TLBa', 'IPC',
				'Total_Instructions', 'Total_Cycles',
				'L1-Total-Misses', 'L1-Load-Misses', 'L1-Store-Misses',
				'L2-Total-Misses', 'L2-Load-Misses', 'L2-Store-Misses',
				'Tlb-Total-Misses', 'Tlb-Load-Misses', 'Tlb-Store-Misses']
		header = ''
		for key in keys:
			header += key
			header += ';'
		out_string = out_string + header + '\n'
		for i in range(0, len(argv)):
			if os.path.exists(argv[i]):
				with open(argv[i], 'r') as in_file:
					l_key = ''
					try:
						in_stream = yaml.safe_load(in_file)
						line = ''
						for key in keys:
							l_key = key
							line += str(in_stream[key])
							line += ';'
						out_string = out_string + line + '\n'
					except KeyError:
						sys.stderr.write("--Error-- {} does not contain key: {}.\n".format(argv[i], l_key))
						flag = False
			else:
				sys.stderr.write("File {} does not exist.".format(argv[i]))
		if flag:
			print('Process finished without errors.')
			return out_string
		else:
			sys.stderr.write('Process finished with errors.' + '\n')
			return False
