f = open('film.csv', 'r')
count = 0
while True:
	line = f.readline()
	if line == '':
		break
	fields = line.split(';')
	if fields[3] == 'Comedy':
		count += 1
print(count)
