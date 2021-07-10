import math

def polar2cart(R,theta):
	#function for coonverting polar coordinates to cartesian
	print('New Coordinates: ', R*math.cos(theta), R*math.sin(theta))

def cart2polar(x,y):
	#function for coonverting cartesian coordinates to polar
	print('New Coordinates: ', (x**2+y**2)**(0.5), math.atan(y/x))

print('Convert Coordinates')
print('Polar to Cartesian? Put 1. Cartesian to Polar? Put 2.')

ip=int(input('Your wish: ')) #prompt user for input

if ip==1:
	#if user enters 1, execute this block
	R=int(input('Enter R= '))
	theta=(input('Enter theta in radians= '))
	polar2cart(R,theta)
else:
	#if user does not enter 1, execute this block
	x=int(input('Enter x= '))
	y=int(input('Enter y= '))
	cart2polar(x,y)
