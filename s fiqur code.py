def print_S():
    """Prints the pattern for the letter 'S'."""
    for row in range(7):
      if row ==0 or row ==3 or row ==6:
         print("*****")
      elif row<3:
         print("*   ")
      else:
         print("    *")

print("Pattern for S:")
print_S()