def evil(n):
  binary_number = format(n,'b')
  binary_string = str(binary_number)
  even_counter = 0
  for number in binary_string:
    if number == '1': even_counter += 1
  if even_counter % 2 == 0: return "It's Evil!"
  else: return "It's Odious!"

print (f"resultado para n = 1  ==> {evil(1)} || esperado It's Odious!")
print (f"resultado para n = 2  ==> {evil(2)} || esperado It's Odious!")
print (f"resultado para n = 3  ==> {evil(3)} || esperado It's Evil!")
