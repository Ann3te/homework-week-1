# import math module so we can use deg, cos, tan

import math
from math import degrees

# assign value for each equation variable
gravity = 9.81
vel_initial = 44
barrel_height = 1
distance = 0.5

theta_deg = 80
# convert the value of theta to radians (manually)
# theta_rad = theta_deg * (math.pi/180)

# convert the value of theta to radians (using function from math module)
theta_rad = math.radians(theta_deg)

# calculate y
projectile_height = barrel_height + (distance * math.tan(theta_rad)) - ((gravity * distance**2)/(2 * (vel_initial * math.cos(theta_rad))**2))

# round the answer to 2 dp
final_answer = round(projectile_height, 2)

# print answer
print("y =", final_answer, "metres")
