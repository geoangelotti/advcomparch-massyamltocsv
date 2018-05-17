import massyamltocsv

with open('files/Out.csv', 'w+') as out_file:
	out_file.write(massyamltocsv.getcsv(['files/Pr_1.yaml', 'files/Pr_2.yaml']))
