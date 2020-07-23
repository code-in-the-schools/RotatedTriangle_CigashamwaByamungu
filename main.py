#UserInputFunctions
L1 = input("Enter any character:")
L2 = int(input("Enter any positive number(<50):"))

#180 Rotation Attempt
def pyramid(p):

   X = 1*p - 1

   for m in range(0, p):
      for n in range(0, X):
         print(end=" ")

      X = X - 1

      for n in range(0, m+1):
         print(L1, end="")
      print("\r")

p = L2
pyramid(p)