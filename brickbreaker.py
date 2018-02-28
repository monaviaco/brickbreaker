#
# final.py
#
#
# Name: Monica Acosta & Grace Breckenridge
#

from visual import *
import random


def make_walls():
	""" makes several walls and returns them in a list
		Docs here:  http://vpython.org/contents/docs/box.html
	"""
	w0 = box(pos=(-20,0,5), axis=(0,0,1), # creates left wall
			 length=50, width=1, height = 1, color=color.white)
	w1 = box(pos=(0,0,-20), axis=(1,0,0), # creates top wall
			 length=40, width=1, height = 1, color=color.white)
	w2 = box(pos=(20,0,5), axis=(0,0,1), # creates right wall
			 length=50, width=1, height=1, color=color.white)
	list_of_walls = [ w0, w1, w2 ]
	return list_of_walls


def make_paddle():
	""" makes a paddle!
	"""
	paddle = box(pos=(0,.75,29), length=10, height=2, width=1, color=color.red) # creates paddle
	return paddle


def bricks():
	""" makes the bricks!
	"""
	b1 = box(pos=(16,0,-18), length=8, height=1, width=3, color=color.cyan)         # creates row 1
	b2 = box(pos=(8,0,-18), length=8, height=1, width=3, color=color.cyan)
	b3 = box(pos=(0,0,-18), length=8, height=1, width=3, color=color.cyan)
	b4 = box(pos=(-8,0,-18), length=8, height=1, width=3, color=color.cyan)
	b5 = box(pos=(-16,0,-18), length=8, height=1, width=3, color=color.cyan)
	
	b6 = box(pos=(16,0,-15), length=8, height=1, width=3, color=color.blue)      # creates row 2
	b7 = box(pos=(8,0,-15), length=8, height=1, width=3, color=color.blue)
	b8 = box(pos=(0,0,-15), length=8, height=1, width=3, color=color.blue)
	b9 = box(pos=(-8,0,-15), length=8, height=1, width=3, color=color.blue)
	b10 = box(pos=(-16,0,-15), length=8, height=1, width=3, color=color.blue)
	
	b11 = box(pos=(16,0,-12), length=8, height=1, width=3, color=color.magenta)     # creates row 3
	b12 = box(pos=(8,0,-12), length=8, height=1, width=3, color=color.magenta)
	b13 = box(pos=(0,0,-12), length=8, height=1, width=3, color=color.magenta)
	b14 = box(pos=(-8,0,-12), length=8, height=1, width=3, color=color.magenta)
	b15 = box(pos=(-16,0,-12), length=8, height=1, width=3, color=color.magenta)
	
	b16 = box(pos=(16,0,-9), length=8, height=1, width=3, color=color.red)      # creates row 4
	b17 = box(pos=(8,0,-9), length=8, height=1, width=3, color=color.red)
	b18 = box(pos=(0,0,-9), length=8, height=1, width=3, color=color.red)
	b19 = box(pos=(-8,0,-9), length=8, height=1, width=3, color=color.red)
	b20 = box(pos=(-16,0,-9), length=8, height=1, width=3, color=color.red)
	
	b21 = box(pos=(16,0,-6), length=8, height=1, width=3, color=color.orange)      # creates row 5
	b22 = box(pos=(8,0,-6), length=8, height=1, width=3, color=color.orange)
	b23 = box(pos=(0,0,-6), length=8, height=1, width=3, color=color.orange)
	b24 = box(pos=(-8,0,-6), length=8, height=1, width=3, color=color.orange)
	b25 = box(pos=(-16,0,-6), length=8, height=1, width=3, color=color.orange)

	b26 = box(pos=(16,0,-3), length=8, height=1, width=3, color=color.yellow)         # creates row 6
	b27 = box(pos=(8,0,-3), length=8, height=1, width=3, color=color.yellow)
	b28 = box(pos=(0,0,-3), length=8, height=1, width=3, color=color.yellow)
	b29 = box(pos=(-8,0,-3), length=8, height=1, width=3, color=color.yellow)
	b30 = box(pos=(-16,0,-3), length=8, height=1, width=3, color=color.yellow)
	
	b31 = box(pos=(16,0,0), length=8, height=1, width=3, color=color.green)      # creates row 7
	b32 = box(pos=(8,0,0), length=8, height=1, width=3, color=color.green)
	b33 = box(pos=(0,0,0), length=8, height=1, width=3, color=color.green)
	b34 = box(pos=(-8,0,0), length=8, height=1, width=3, color=color.green)
	b35 = box(pos=(-16,0,0), length=8, height=1, width=3, color=color.green)
	
	b36 = box(pos=(16,0,3), length=8, height=1, width=3, color=color.cyan)     # creates row 8
	b37 = box(pos=(8,0,3), length=8, height=1, width=3, color=color.cyan)
	b38 = box(pos=(0,0,3), length=8, height=1, width=3, color=color.cyan)
	b39 = box(pos=(-8,0,3), length=8, height=1, width=3, color=color.cyan)
	b40 = box(pos=(-16,0,3), length=8, height=1, width=3, color=color.cyan)
	
	b41 = box(pos=(16,0,6), length=8, height=1, width=3, color=color.blue)      # creates row 9
	b42 = box(pos=(8,0,6), length=8, height=1, width=3, color=color.blue)
	b43 = box(pos=(0,0,6), length=8, height=1, width=3, color=color.blue)
	b44 = box(pos=(-8,0,6), length=8, height=1, width=3, color=color.blue)
	b45 = box(pos=(-16,0,6), length=8, height=1, width=3, color=color.blue)
	
	b46 = box(pos=(16,0,9), length=8, height=1, width=3, color=color.magenta)      # creates row 10
	b47 = box(pos=(8,0,9), length=8, height=1, width=3, color=color.magenta)
	b48 = box(pos=(0,0,9), length=8, height=1, width=3, color=color.magenta)
	b49 = box(pos=(-8,0,9), length=8, height=1, width=3, color=color.magenta)
	b50 = box(pos=(-16,0,9), length=8, height=1, width=3, color=color.magenta)
	
	list_of_boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42, b43, b44, b45, b46, b47, b48, b49, b50]
	return list_of_boxes


def main():
	""" this is the main function, including
		all of the data objects and the "event loop"
		which is the while True
	"""

	scene.range = 36 # RANGE OF STARTING VIEW
	scene.forward = vector(0,-1,-.5) # STARTING VIEW
	scene.autoscale = False
	RATE = 100
	dt = 1.0/RATE

	# create an object named floor of class (type) box:
	floor = box(pos=(0,-1,0), length=40, width=40, height = 0.5, color=color.black)

	Walls = make_walls() # creates a list of walls
	w0, w1, w2 = Walls   # and gives each one a name...

	ball = sphere( radius=1, pos=(0,0,28), color=(1,0.7,0.2)) # creates the ball
	ball.vel = vector(0,0,0) # gives the ball a starting velocity

	paddle = make_paddle() #creates paddle
	paddle.vel = vector(0,0,0)   # gives paddle 0 velocity at beginning of game


	txt = text(text="GAME OVER!",height=5, pos= (-22.5,10,-22), axis=(100,0,0), depth=-.03,color=color.yellow) # 'losing' text object
	txt.visible = False

	txtbeneath = text(text="Exit out of window to play again.",height=2, pos= (-20,5,-22), axis=(100,0,0), depth=-.03,color=color.magenta) # 'losing' text object
	txtbeneath.visible = False

	#txtowners = text(text="Proud owners of this game: Grace & Monica",height=1, pos= (-20,20,-22), axis=(100,0,0), depth=-.03,color=color.cyan) # 'losing' text object
	#txtowners.visible = False

	txt1 = text(text="Press SPACE to begin.",height=3, pos= (-20,10,-22), axis=(100,0,0), depth=-.03,color=color.cyan) # 'starting' text object
	txt1.visible = True

	txt2 = text(text="YOU WON!",height=5, pos= (-20.5,10,-22), axis=(100,0,0), depth=-.03,color=color.yellow) # 'winning' text object
	txt2.visible = False

	Bricks = bricks() # defines bricks and adds them to Brick
	b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42, b43, b44, b45, b46, b47, b48, b49, b50 = Bricks
	# we set some variables to control the display and the event loop

	RATE = 100             # number of loops per second to run, if possible!
	dt = 1.0/(1.0*RATE)   # the amount of time per loop (again, if possible)
	autocenter = True     # do you want vPython to keep the scene centered?

	RAT = 100           # number of loops per second to run, if possible!
	dt = 1.0/(1.0*RAT)   # the amount of time per loop (again, if possible)
	autocenter = True     # do you want vPython to keep the scene centered?

	BALL = [ball]

	# this is the main loop of the program! it's "time" or the "event loop"
	
	while True:
		rate(RATE)     # run no faster than RATE loops/second
		
		if scene.kb.keys:            # begins key event if-statement
			s = scene.kb.getkey()    # imports keypress function
			#print "keypress is", s
			if s == " ":             # if you press a space, it begins the ball
				txt1.visible = False
				print "starting ball..."
				ball.vel = vector(-10,0,-10) #sets the direction the ball will begin going towards


		for b in BALL:
			b.pos += dt*b. vel
			# check if the ball goes beyond the paddle
			if mag( b.pos ) > 40:  # a bit bigger than the box
				b.visible = False  # make invisible  # remove from list
				paddle.vel = vector(0,0,0) # starts paddle at starting velocity
				paddle.pos = vector(0,.75,29) # starts paddle at starting position
				ball.vel = vector(0,0,0) # starts ball at starting velocity
				ball.pos = vector(0,0,28) # starts ball at starting position
				ball.visible = True # makes the ball visible again
				if len(Bricks) == 0:
					txt.visible = False # keeps 'losing' txt invisible if game is won
					txt.beneath = False # keeps 'beneath' txt invisible if game is won
					txt2.visible = True # makes 'winning' txt visible if game is won
				else:
					txt.visible = True # makes 'losing' txt visible if game is lost
					txtbeneath.visible = True #keeps 'beneath' txt invisible if game is won
					#txtowners.visible = True #keeps 'owner' txt invisible if game is won
					txt2.visible = False # keeps 'winning' txt invisible if game is lost


		# +++++ start of all position updates: once per loop +++++ 

		ball.pos = ball.pos + ball.vel*dt

		# +++++ end of all once-per-loop position updates +++++ 




		# ----- start of *collisions*  -----
		
		# paddle colliding with wall 0, w0:
		if paddle.pos.x < w0.pos.x:  # w0 has the smallest x value
			paddle.pos.x = w0.pos.x  # make sure we stay in bounds
			paddle.vel.x = -1.0 * paddle.vel.x   # bounce (in the x direction)

		# paddle colliding with wall 2, w2:
		if paddle.pos.x > w2.pos.x-1:
			paddle.pos.x = w2.pos.x-1
			paddle.vel.x = -1.0 * paddle.vel.x

		# ball colliding with wall 1, w1:
		if ball.pos.z < w1.pos.z:
			ball.pos.z = w1.pos.z
			ball.vel.z = -1.0 * ball.vel.z
		
		# ball colliding with wall 0, w0:
		if ball.pos.x < w0.pos.x+1:  # w0 has the smallest x value
			ball.pos.x = w0.pos.x +1 # make sure we stay in bounds
			ball.vel.x = -1.0 * ball.vel.x   # bounce (in the x direction)
		
		# ball colliding with wall 2, w2:
		if ball.pos.x > w2.pos.x-1:
			ball.pos.x = w2.pos.x-1
			ball.vel.x = -1.0 * ball.vel.x

		# ball colliding with paddle:
		if ball.pos.z > paddle.pos.z - 1.5 and ball.pos.z < paddle.pos.z + 1.5: #this is for the padddle bounce
			if ball.pos.x < paddle.pos.x + 5 and ball.pos.x > paddle.pos.x - 5 :
				ball.pos.z = paddle.pos.z - 1.5
				ball.vel.z = -1.0 * ball.vel.z

		# ball colliding with each brick, makes brick disappear when hit
		for i in Bricks:
			if ball.pos.z < i.pos.z + 1.5 and ball.pos.z > i.pos.z - 1.5:
				if ball.pos.x < i.pos.x + 5 and ball.pos.x > i.pos.x - 5 :
					ball.pos.z = i.pos.z + 1.5
					ball.vel.z = -1.0 * ball.vel.z
					i.visible = False
					Bricks.remove(i)

		# ----- end of *collisions*  -----



		rate(RAT)
		# ===== handling user events: keypresses and mouse =====

		# here, we see if the user has pressed any keys
		if scene.kb.keys:   # any keypress to be handled?
			s = scene.kb.getkey()
			print "You pressed the key", s  

			# Key presses to give the paddle velocity (in the x-z plane)
			if s == 'left': paddle.pos.x += -5
			if s == 'right': paddle.pos.x += 5

			if s == 'q':  # Quit!
				print "Quitting..."
				break  # breaks out of the main loop

		# ===== end of handling user events: keypresses and mouse =====

	print "Game Over!"
	print "Close the vPython window to finish."


if __name__ == "__main__":
	main()                   







