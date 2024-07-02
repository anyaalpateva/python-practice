import math

def calculate(value):
  if value < 0:
    raise ValueError("Value cannot be lower that zero.")
  return math.factorial(value)

def main():
  while True:
    user_input = input("(INPUT) Enter value (or q to quit): ")
    if user_input.lower() == "q":
      break
    try:
      number = int(user_input)
      result = calculate(number)
      print(f"(RESULT) Factorial of {number} is {result}")
    except ValuerError as e:
      print(f"(ERROR): {e}")

if __name__ == "__main__":
  main()
