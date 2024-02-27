def same_case(a, b): 
  if not a.isalpha() or not b.isalpha(): return -1
  if a.isupper() == b.isupper() or a.islower() == b.islower(): return 1
  return 0



print (f"Resultado para a = G y b = a -- Resultado = {same_case('G','a')}")
