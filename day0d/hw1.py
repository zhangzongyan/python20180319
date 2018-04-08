

class Screen(object):
	@property   #getter	
	def mywidth(self):
		return self._width

	@mywidth.setter	
	def mywidth(self, w):
		self._width = w 
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, h):
		self._height = h
	@property
	def area(self):
		return self._width * self._height

s = Screen()
s.mywidth = 100
s.height = 200
print("h:{}, w:{}, area:{}".format(s.mywidth, s.height, s.area))



