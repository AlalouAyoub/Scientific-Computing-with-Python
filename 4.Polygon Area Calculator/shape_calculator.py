class Rectangle:

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def set_width(self, x):
		self.width = x

	def set_height(self, y):
		self.height = y

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return 2 * self.width + 2 * self.height

	def get_diagonal(self):
		return (self.width ** 2 + self.height ** 2) ** 0.5

	def get_picture(self):
		if self.height > 50 or self.width > 50:
			return "Too big for picture."
		else:
			output = ''
			for i in range(self.height):
				output += f"{'*' * self.width}\n"
			return output

	def get_amount_inside(self, shape):
		if isinstance(shape, Rectangle):
			return self.get_area() // shape.get_area()
		else:
			return f'{shape} is invalid'

	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

	def __init__(self, side):
		super().__init__(side, side)

	def set_side(self, new_side):
		self.height = new_side
		self.width = new_side

	def __str__(self):
		return f'Square(side={self.width})'

   
