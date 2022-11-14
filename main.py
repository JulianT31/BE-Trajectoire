import math  # Optionally
import latexify

@latexify.function
def solve(a, b, c):
  return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

print(solve(1, 4, 3))  # Invoking the function works as expected.
print(solve)  # Printing the function shows the underlying LaTeX expression.
