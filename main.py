import sys
import yaml
import os


def main():
	if len(sys.argv) == 1:
		print("Usage: python main.py <in> (<in'> ...)")
	else:
		flag = True
		with open('Out.csv', 'w+') as out_file:
			columns = ['L1c', 'L1b', 'L1a', 'L2c', 'L2b', 'L2a', 'L2prf', 'TLBe', 'TLBp', 'TLBa', 'IPC',
					   'Total_Instructions', 'Total_Cycles',
					   'L1-Total-Misses', 'L1-Load-Misses', 'L1-Store-Misses',
					   'L2-Total-Misses', 'L2-Load-Misses', 'L2-Store-Misses',
					   'Tlb-Total-Misses', 'Tlb-Load-Misses', 'Tlb-Store-Misses']
			header = ''
			for cell in columns:
				header += cell
				header += ';'
			out_file.write(header + '\n')
			for i in range(1, len(sys.argv)):
				if os.path.exists(sys.argv[i]):
					with open(sys.argv[i], 'r') as in_file:
						global_cell = ''
						try:
							in_stream = yaml.safe_load(in_file)
							out_stream = ''
							for cell in columns:
								global_cell = cell
								out_stream += str(in_stream[cell])
								out_stream += ';'
							out_file.write(out_stream + '\n')
						except KeyError:
							print("--Error-- {} does not contain key: {}.".format(sys.argv[i], global_cell))
							flag = False
				else:
					print("{} does not exist.".format(sys.argv[i]))
		if flag:
			print('Process finished without errors.')
		else:
			print('Process finished with errors.')
			os.remove('Out.csv')


main()
