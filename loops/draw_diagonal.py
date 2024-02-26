dim = int(input("Dumension de la matriz: "))
for x in range(dim):
  for y in range(dim):
    if x < y:
      symbol = "U"
    elif x > y: 
      symbol = "D"
    else:
      symbol = "X"
    print(symbol, end=' ')
  print()