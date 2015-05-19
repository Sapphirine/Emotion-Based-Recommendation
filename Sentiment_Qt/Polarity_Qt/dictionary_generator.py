f = open("positive-words.txt", 'r')
output = open("positive.yml", 'w')

while 1:
	line = f.readline()
	if not line:
		break
	output.write(line[:-1].decode('ascii', 'ignore') + ": [positive]\n")

f.close()
output.close()

f = open("negative-words.txt", 'r')
output = open("negative.yml", 'w')

while 1:
	line = f.readline()
	if not line:
		break
	output.write(line[:-1].decode('ascii', 'ignore') + ": [negative]\n")

f.close()
output.close()
