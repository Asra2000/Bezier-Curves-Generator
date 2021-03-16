import pygame as py
from main import *

class Curves(object):

	def linear_curve(self, screen, points, color, t, reference = False):
		# b(T) = (1-t)p0+ tp1
		P0_X = (1-t) * points[0].x
		P0_Y = (1-t) * points[0].y
		P1_X = t * points[1].x
		P1_Y = t * points[1].y

		curve = (P0_X + P1_X, P0_Y + P1_Y)
		# print(curve, t)
		if reference:
			py.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 5)
			return (int(curve[0]), int(curve[1]))

		else:
			py.draw.line(screen, WHITE, (points[0].x, points[0].y), (points[1].x, points[1].y), 1)
			py.draw.line(screen, color, (points[0].x, points[0].y), (int(curve[0]), int(curve[1])), 5)
			py.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 5)


	def quadratic_curve(self, screen, points, color, t, curve_list):
		GREEN = (0, 255, 0)
		P0_X = (1-t)**2 * points[0].x
		P0_Y = (1-t)**2 * points[0].y

		P1_X = 2 * (1-t) * t * points[1].x
		P1_Y = 2 * (1-t) * t  * points[1].y
		
		P2_X = t**2 * points[2].x
		P2_Y = t**2 * points[2].y

		curve = (P0_X + P1_X + P2_X, P0_Y + P1_Y + P2_Y)
		py.draw.line(screen, WHITE, (points[0].x, points[0].y), (points[1].x, points[1].y), 1)
		py.draw.line(screen, WHITE, (points[1].x, points[1].y), (points[2].x, points[2].y), 1)

		a = self.linear_curve(screen, [points[0], points[1]], LIGHT_BLUE, t, True)
		b = self.linear_curve(screen, [points[1], points[2]], LIGHT_BLUE, t, True)

		py.draw.line(screen, LIGHT_BLUE, a, b, 1)
		py.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 5)

		curve_list.append((int(curve[0]), int(curve[1])))

	def cubic_curve(self, screen, points ,color, t, curve_list):
		GREEN = (0, 255, 0)
		BLUE = (0, 0, 230)
		P0_X = (1-t)**3 * points[0].x
		P0_Y = (1-t)**3 * points[0].y
		P1_X = 3 * (1-t)**2 * t * points[1].x
		P1_Y = 3 * (1-t)**2 * t  * points[1].y
		P2_X = 3 * (1-t) * t**2 * points[2].x
		P2_Y = 3 * (1-t) * t**2 * points[2].y
		
		P3_X = t**3 * points[3].x
		P3_Y = t**3 * points[3].y

		curve = (P0_X + P1_X + P2_X + P3_X, P0_Y + P1_Y + P2_Y + P3_Y)

		#lines
		py.draw.line(screen, WHITE, (points[0].x, points[0].y), (points[1].x, points[1].y), 1)
		py.draw.line(screen, WHITE, (points[1].x, points[1].y), (points[2].x, points[2].y), 1)
		py.draw.line(screen, WHITE, (points[2].x, points[2].y), (points[3].x, points[3].y), 1)

		#refernce line
		a = self.linear_curve(screen, [points[0], points[1]], LIGHT_BLUE, t, True)
		b = self.linear_curve(screen, [points[1], points[2]], LIGHT_BLUE, t, True)
		c = self.linear_curve(screen, [points[2], points[3]], LIGHT_BLUE, t, True)

		py.draw.line(screen, LIGHT_BLUE, a, b, 1)
		py.draw.line(screen, LIGHT_BLUE, b, c, 1)

		#reference quadratic
		quad_list1 = []
		quad_list2 = []
		self.quadratic_curve(screen, [points[0], points[1], points[2]], FADED_BLUE, t, quad_list1)
		self.quadratic_curve(screen, [points[1], points[2], points[3]], FADED_BLUE, t, quad_list2)
		py.draw.line(screen, FADED_BLUE, quad_list1[0], quad_list2[0], 1)
		py.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 5)
		curve_list.append((int(curve[0]), int(curve[1])))



        
