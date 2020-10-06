def traspuesta(M,n): 
  B = [] 
  for i in range(n): 
    B.append([])
    for j in range(n): 
      B[i].append(0)
  for i in range(n):
    for j in range(n): 
      B[j][i]=M[i][j]

  return B 
n=int(input()) 
M=[]
for i in range(n):
  M.append([]) 
  for j in range(n): 
    M[i].append(int(input()))

print(traspuesta(M,n))
