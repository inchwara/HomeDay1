class Ball(object):

	def __init__(self):
		self.velocity = (0,0)
		self.position = (20,20)

	def bounce(self):
		self.velocity = (self.velocity[0],-self.velocity[1])

	ball1 = Ball()
	ball1.velocity = (5,10)
	ball1.position = (30,30)