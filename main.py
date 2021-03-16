import pygame as py
from curve import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (120, 120, 120)
BLUE = (0, 0, 255)
PINK = (252, 209, 209)
GREY1 = (236, 226, 225)
LIGHT_BLUE = (174, 225, 225)
FADED_BLUE = (238, 235, 221)

class Position():
	def __init__(self, x, y, name = " "):
		self.x = x
		self.y = y
		self.name = name

	def draw(self, screen, font):
		text = font.render(self.name, True, WHITE)
		text_rect = text.get_rect()
		if self.y >= 300:
			text_rect.center = (self.x, self.y+30)
		else:
			text_rect.center = (self.x, self.y-30)

		screen.blit(text,text_rect)



		py.draw.circle(screen, GREY1, (self.x, self.y), 5)
		py.draw.circle(screen, WHITE, (self.x, self.y), 3)
        

class Environment(object):
	
	"""main env class"""
	def __init__(self):
		self.height = 600
		self.width = 1000
		self.screen = py.display.set_mode((self.width, self.height))
		py.display.set_caption("Bezier Curves")

	def draw(self):
		self.screen.fill(BLACK)

	def blit_text(self, font, pos, color, text):
		lines = text.splitlines()
		for i, line in enumerate(lines):
			self.screen.blit(font.render(line, True, color), (pos[0],pos[1]+i*20))



if __name__ == '__main__':
	py.init()
	font = py.font.Font('freesansbold.ttf', 20)
	font1 = py.font.Font('freesansbold.ttf', 12)
	env = Environment()
	curve = Curves()
	linear_points = [Position(40, 260, "P0"), Position(200, 140, "P1")]
	linear_text = "The t in the function for a linear Bézier curve\n can be thought of as describing\n how far B(t) is from P0 to P1.\n For example, when t=0.25, B(t) is one quarter\n of the way from point P0 to P1.\n As t varies from 0 to 1, B(t)\n describes a straight line from P0 to P1."
	
	quadratic_points = [Position(330, 260, "P0"), Position(400, 120, "P1"), Position(450, 400, "P2")]
	quad_text = "For quadratic Bézier curves one can construct \nintermediate points Q0 and Q1 such that \nas t varies from 0 to 1:Point Q0(t) varies from P0 to P1 \nand describes a linear Bézier curve.\
	\nPoint Q1(t) varies from P1 to P2 and describes a linear Bézier curve.\
	\nPoint B(t) is interpolated linearly between \nQ0(t) to Q1(t) and describes a quadratic Bézier curve"
	
	cubic_points = [Position(600, 260, "P0"), Position(660, 120, "P1"), Position(740, 300, "P2"), Position(800, 140, "P3")]
	cube_text = "Four points P0, P1, P2 and P3 in the plane or in \nhigher-dimensional space define \na cubic Bézier curve.\n The curve starts at P0 going toward P1 and \narrives at P3 coming from the direction of P2. "
	curve_quadratic = []
	curve_cubic = []

	run = True
	clock = py.time.Clock()
	t = 0
	while run:
		for event in py.event.get():
			if event.type == py.QUIT:
				run = False
		env.draw()

		env.blit_text(font, (10, 10), PINK, "BEZIER CURVES")

		env.blit_text(font, (40, 270), LIGHT_BLUE, "Linear Curve")
		env.blit_text(font1, (40, 300), FADED_BLUE, linear_text)

		env.blit_text(font, (340, 440), LIGHT_BLUE, "Quadratic Curve")
		env.blit_text(font1, (340, 460), FADED_BLUE, quad_text)

		env.blit_text(font, (700, 350), LIGHT_BLUE, "Cubic Curve")
		env.blit_text(font1, (700, 380), FADED_BLUE, cube_text)

		curve.linear_curve(env.screen, linear_points, PINK, t)
		curve.quadratic_curve(env.screen, quadratic_points, PINK, t, curve_quadratic)
		curve.cubic_curve(env.screen, cubic_points, PINK, t, curve_cubic)

		for point in linear_points:
			point.draw(env.screen, font)


		for point in quadratic_points:
			point.draw(env.screen, font)

		for point in cubic_points:
			point.draw(env.screen, font)


		if len(curve_quadratic) > 2:
			py.draw.lines(env.screen, PINK, False, curve_quadratic, 5)

		if len(curve_cubic) > 2:
			py.draw.lines(env.screen, PINK, False, curve_cubic, 5)

		t = t + 0.005
		if t > 1:
			t = 0
			curve_quadratic.clear()
			curve_cubic.clear()

		py.display.update()
		clock.tick(60)



	py.quit()
