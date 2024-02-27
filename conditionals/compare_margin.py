def close_compare(a, b, margin=0):
  if margin >= abs(a-b): return 0
  elif a < b: return -1
  else: return 1
  


  '''

  comparar si a es close to b 
  a es close de b si margin >= distancia absoluta entre a y b -> abs(a-b)  en este caso return 0
  SINO: 2 escenarios
        - a < b return -1 
        - a > b return 1 

  '''
  
print (f"resultado para a = 4 | b = 5 | margin = NULL ==> {close_compare(4, 5)} || esperado -1") # -1
print (f"resultado para a = 5 | b = 5 | margin = NULL ==> {close_compare(5, 5)} || esperado 0") # 0
print (f"resultado para a = 6 | b = 5 | margin = NULL ==> {close_compare(6, 5)} || esperado 1") # 1

print (f"resultado para a = 6 | b = 5 | margin = NULL ==> {close_compare(2, 5, 3)} || esperado 0") # 0
print (f"resultado para a = 6 | b = 5 | margin = NULL ==> {close_compare(5, 5, 3)} || esperado 0") # 0
print (f"resultado para a = 6 | b = 5 | margin = NULL ==> {close_compare(8, 5, 3)} || esperado 0") # 0
print (f"resultado para a = 6 | b = 5 | margin = NULL ==> {close_compare(8.1, 5, 3)} || esperado 1") # 1
print (f"resultado para a = 6 | b = 5 | margin = NULL ==> {close_compare(1.99, 5, 3)} || esperado -1") # -1

