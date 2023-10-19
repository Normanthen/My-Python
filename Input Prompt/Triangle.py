def calculate_triangle_area(base, height):
  """Calculates the area of a triangle.

  Args:
    base: The length of the base of the triangle.
    height: The height of the triangle.

  Returns:
    The area of the triangle.
  """

  area = (base * height) / 2

  return area


def main():
  """Prompts the user for the length and height of a triangle and then calculates the area of the triangle."""

  # Prompt the user for the length of the base.
  base = float(input("Enter the length of the base of the triangle: "))

  # Prompt the user for the height of the triangle.
  height = float(input("Enter the height of the triangle: "))

  # Calculate the area of the triangle.
  area = calculate_triangle_area(base, height)

  # Print the area of the triangle to the console.
  print(f"The area of the triangle is {area:.2f} square units.")


if __name__ == "__main__":
  main()
