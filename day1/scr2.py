movements = []
with open('in.txt') as f:
  for line in f.readlines():
    movements.append(int(line[1:]) if line[0] == 'R' else -int(line[1:]))

start = 50
counter = 0

for move in movements:
  zero = start != 0
  start += move
  if start == 0:
    counter +=1 
  elif start >=100:
    counter += start // 100
  elif start < 0:
    counter += start // -100 + zero
  start %= 100


print(counter)
