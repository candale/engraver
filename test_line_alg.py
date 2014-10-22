import time

# current position
pos_x = 0 
pos_y = 0


def moveto(new_x, new_y, steps_per_second):
	'''
		Generates points that go from the initial point to the newly given point
		Params:
		The new x and y that the pointer should move to
	'''

	global pos_x
	global pos_y

	# difference between the current and new points
	delta_x = new_x - pos_x
	delta_y = new_y - pos_y

	# direction for each axis
	dir_x = 1 if delta_x > 0 else -1
	dir_y = 1 if delta_y > 0 else -1

	# get the absolute values so we can use them
	delta_x = abs(delta_x)
	delta_y = abs(delta_y)

	# the counter that, when overflows, steps the other motor
	axis_counter = 0
	counter = 0

	if delta_x > delta_y:
		while counter <  delta_x:
			pos_x += dir_x
			axis_counter += delta_y
			if axis_counter >= delta_x:
				axis_counter -= delta_x
				pos_y += dir_y

			time.sleep(1.0 / steps_per_second)
			counter += 1
			print "X:", pos_x, " X:", pos_y

		
	else:
		while counter < delta_y:
			pos_y += dir_y
			axis_counter += delta_x
			if axis_counter >= delta_y:
				axis_counter -= delta_y
				pos_x += dir_x

			time.sleep(1.0 / steps_per_second)
			counter += 1

			print "X:", pos_x, " X:", pos_y	


moveto(100, 100, 100)