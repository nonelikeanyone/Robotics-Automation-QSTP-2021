import math

def polar2cart(R,theta):
	print('New Coordinates: ', R*math.cos(theta), R*math.sin(theta))

def cart2polar(x,y):
	print('New Coordinates: ', (x**2+y**2)**(0.5), math.atan(y/x))

print('What do you want?')
print('Polar to Cartesian? Put 1. Cartesian to Polar? Put 2.')

ip=int(input('Your wish: '))

if ip==1:
	R=int(input('Enter R= '))
	theta=(input('Enter theta in radians= '))
	polar2cart(R,theta)
else:
	x=int(input('Enter x= '))
	y=int(input('Enter y= '))
	cart2polar(x,y)
