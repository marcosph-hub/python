def get_real_floor(n):
  if n <= 0: return n
  elif n < 13: return n - 1
  elif n > 13: return n - 2


print(f"piso not americana: {-2} - piso not europea {get_real_floor(-2)}")
print(f"piso not americana: {10} - piso not europea {get_real_floor(10)}")
print(f"piso not americana: {12} - piso not europea {get_real_floor(12)}")
print(f"piso not americana: {16} - piso not europea {get_real_floor(16)}")
  