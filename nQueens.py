class solution:

  #initalizing a list with 20 positions as zero
  def __init__(self):
    self.MAX = 20
    self.A = [0]*self.MAX

  #Checking if the current poition of queen clashes with any of the previous queens
  # (self.A[k] == j) to check the condition vertically
  # abs(self.A[k] - j) == abs(k - i) to check the condition horizontally
  def placement(self,i,j):
    for k in range(1,i):
      if (self.A[k] == j) or abs(self.A[k] - j) == abs(k - i):
        return False
    return True

  #To print the solution for the problem
  def printplacequeen(self,N):
    print('Arrangement-->\n')
    for i in range(1,N+1):
      for j in range(1,N+1):
        if self.A[i] != j:
          print('\t_',end='')
        else:
          print('\tQ',end = '')
      print('\n\n')

  #recursive function
  def N_Queens(self,i,N):
    for k in range(1,N+1):
      if self.placement(i,k):
        self.A[i] = k
        if i==N:
          self.printplacequeen(N)
        else:
          self.N_Queens(i+1,N)


N = int(input('Enter the no. of Queens: '))
#condition for no solutions
if N==2 or N==3 :
  print("No solution")
else:
  obj = solution()
  obj.N_Queens(1,N)
