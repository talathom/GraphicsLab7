# maze.py starter Code

import viz
import vizshape
import vizcam
import math

# An instance of this class adds a maze to the scene along with 
# an avatar that can be navigated through it.
class Maze(viz.EventClass):

	# Constructor 
	def __init__(self):
		# base class constructor 
		viz.EventClass.__init__(self)
		
		# set up keyboard and timer callback methods
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		
		# avatar's x,z location in maze and its rotation angle
		self.theta = 0
		self.x = 0.5
		self.z = 0.5
		self.fp = False
				
		# The 2D array below stores the representation of a maze.
		# Array entries containing a 2 represent 1 x 2 x 1 wall blocks.
		# Array entries containing a 0 represent 1 x 0.1 x 1 floor blocks.
		self.maze = []
		self.maze = [[2,2,2,2,2,2,2,2,2]] + self.maze # row 8
		self.maze = [[2,0,0,0,0,0,0,0,2]] + self.maze # row 7
		self.maze = [[2,0,0,0,0,0,0,0,2]] + self.maze # row 6
		self.maze = [[2,0,0,2,2,2,0,0,2]] + self.maze # row 5
		self.maze = [[2,0,0,2,2,2,0,0,2]] + self.maze # row 4
		self.maze = [[2,0,0,2,2,2,0,0,2]] + self.maze # row 2
		self.maze = [[0,0,0,0,0,0,0,0,2]] + self.maze # row 0
		self.maze = [[0,0,0,0,0,0,0,0,2]] + self.maze # row 1
		self.maze = [[0,0,0,2,2,2,2,2,2]] + self.maze # row 0
		
		# Add +x,+y,+z coordinate axes to scene to help with placing the blocks correctly
		self.addCoordinateAxes()
		
		# Code to create blocks forming the maze goes here
		for x in range(0, len(self.maze)):
			for z in range(0, len(self.maze[0])):
				if self.maze[x][z] == 0:
					block = vizshape.addCube(size=1, color=viz.YELLOW)
					mat = viz.Matrix()
					mat.postScale(1, 0.1, 1)
					mat.postTrans(x+.5, .05, z+.5)
					block.setMatrix(mat)
				elif self.maze[x][z] == 2:
					block = vizshape.addCube(size=1, color=viz.GREEN)
					mat = viz.Matrix()
					mat.postScale(1, 2, 1)
					mat.postTrans(x+.5, 1, z+.5)
					block.setMatrix(mat)
		self.avatar = viz.add('vcc_female.cfg')
		mat = viz.Matrix()
		mat.postTrans(self.x, .1, self.z)
		self.avatar.setMatrix(mat)
		self.avatar.state(1)

					
	# Key pressed down event code.
	def onKeyDown(self,key):
		if key == 'a' or key == viz.KEY_LEFT:
			mat = viz.Matrix()
			self.theta -= 5
			mat.postAxisAngle(0, 1, 0, self.theta)
			mat.postTrans(self.x, .1, self.z)
			self.avatar.setMatrix(mat)
			if self.fp:
				self.firstPerson()
		
		if key == 'd' or key == viz.KEY_RIGHT:
			mat = viz.Matrix()
			self.theta += 5
			mat.postAxisAngle(0, 1, 0, self.theta)
			mat.postTrans(self.x, .1, self.z)
			self.avatar.setMatrix(mat)
			if self.fp:
				self.firstPerson()
			
		if key == 'w' or key == viz.KEY_UP:
			mat = viz.Matrix()
			rad = viz.radians(self.theta)
			self.z += .1*math.cos(rad)
			self.x += .1*math.sin(rad)
			mat.postAxisAngle(0, 1, 0, self.theta)
			mat.postTrans(self.x, .1, self.z)
			self.avatar.setMatrix(mat)
			if self.fp:
				self.firstPerson()
			
		if key == 's' or key == viz.KEY_DOWN:
			mat = viz.Matrix()
			rad = viz.radians(self.theta)
			self.z -= .1*math.cos(rad)
			self.x -= .1*math.sin(rad)
			mat.postAxisAngle(0, 1, 0, self.theta)
			mat.postTrans(self.x, .1, self.z)
			self.avatar.setMatrix(mat)
			if self.fp:
				self.firstPerson()
			
		if key == '1':
			self.fp = False
			view = viz.MainView
			mat = viz.Matrix()
			mat.postAxisAngle(1, 0, 0, 90)
			mat.postTrans(0, 20, 0)
			view.setMatrix(mat)
			
		if key == '2':
			self.fp = False
			view = viz.MainView
			mat = viz.Matrix()
			mat.postAxisAngle(0, 1, 0, -90)
			mat.postAxisAngle(0, 0, 1, 45)
			mat.postTrans(20, 20, 0)
			view.setMatrix(mat)
			
		if key == '3':
			self.firstPerson()
			
	def firstPerson(self):
		self.fp = True
		view = viz.MainView
		mat = viz.Matrix()
		mat.postAxisAngle(0, 1, 0, self.theta)
		mat.postTrans(self.x, 1.6, self.z)
		view.setMatrix(mat)
			
	# Adds coodinate system that originates at (0,0,0) and extends
	# down the +x, +y, and +z directions.  Locations 1 and 2 units
	# in each direction are marked on the axis.
	def addCoordinateAxes(self):
		viz.startLayer(viz.LINES)
		viz.linewidth(7)
		viz.vertexColor( viz.RED )
		# positive y axis
		viz.vertex(0,0,0); 	   viz.vertex(0,20,0)
		#positive x axis
		viz.vertex(0,0,0); 	   viz.vertex(20,0,0)
		#positive z axis
		viz.vertex(0,0,0); 	   viz.vertex(0,0,20)
		#y=1 tick mark
		viz.vertex(-0.25,1,0); viz.vertex(0.25,1,0)
		#y=2 tick mark
		viz.vertex(-0.25,2,0); viz.vertex(0.25,2,0)
		#x=1 tick mark
		viz.vertex(1,0,-.25);  viz.vertex(1,0,.25)
		#x=2 tick mark
		viz.vertex(2,0,-.25);  viz.vertex(2,0,+.25)
		#z=1 tick mark
		viz.vertex(-.25,0,1);  viz.vertex(.25,0,1)
		#z=2 tick mark
		viz.vertex(-.25,0,2);  viz.vertex(.25,0,2)
		viz.endLayer()
		

