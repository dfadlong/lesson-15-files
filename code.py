f = open('animals.txt', 'r')
text = True
while text:
  text = f.readline()
  print(text.strip())
