weekday_number = input("Put a number between 1-7: ")

print(f"Introduced number: {weekday_number}")

match weekday_number:
  case '1':
    print("Sunday")
  case '2':
    print("Monday")
  case '3':
    print("Tuesday")
  case '4':
    print("Wednesday")
  case '5':
    print("Thursday")
  case '6':
    print("Friday")
  case '7':
    print("Saturday")
  case _:
    print("Wrong number enter a number from 1 to 7")