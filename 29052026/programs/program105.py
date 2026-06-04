def factorial(n):
  if n == 0:
    return 1  # Base case: factorial of 0 is 1
  else:
    return n * factorial(n - 1)
