# advcomparch-massyamltocsv
A project to pass the content of simulation yaml files to csv.

### Usage
```sh
# Write in Out.csv the correct metrics from In1.yaml and In2.yaml
with open('Out.csv', 'w+') as out_file:
	out_file.write(massyamltocsv.getcsv(['In1.yaml', 'In2.yaml']))	
```