f = open('animals.txt', 'r')
while True:
  text = f.readline()
  if text == '':
  	break
  print(text.strip())
