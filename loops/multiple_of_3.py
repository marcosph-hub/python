user_number = int(input("Introduce un numero: "))
sum = 0
multiple = 3
number = 0
result = 0
number_list = []
while sum < user_number:
  result = multiple * number
  sum += result
  number += 1
  number_list.append(result)

for list_item in number_list:
  print(list_item, end=' ')
