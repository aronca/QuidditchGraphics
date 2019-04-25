#quidditch.py

import viz
import vizshape
import vizcam
import math
import os
import random

from Model import *


class quidditch(viz.EventClass):
	def __init__(self):
		viz.EventClass.__init__(self)
		
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown)
		self.callback(viz.KEYUP_EVENT, self.onKeyUp)
		self.callback(viz.TIMER_EVENT,self.onTimer)
		self.starttimer(1,1.0/25.0,viz.FOREVER)
		
		
		# avatar's x,z location in space and its rotation angle
		self.theta = 0
		self.alpha = 0
		self.x = 10
		self.z = 45
		self.y = 20
		self.dtheta = 0
		self.dalpha = 0
		self.moving = False
		
		#number of catches made
		self.catches = 0
		
		
		#create models
		self.quadribol = Model('quadribol'+os.sep+'model.osgb')
		self.snitch	= vizshape.addSphere(radius=0.5, slices=20, stacks=20, axis=vizshape.AXIS_Y, color=[0.7,0.5,0])
		self.broom =  vizshape.addCylinder( height=10, radius=.3 )
		
		
		#texture mapping on sky cube for background
		sky = viz.add(viz.ENVIRONMENT_MAP,'mountsky\mount.jpg')
		skybox = viz.add('skydome.dlc')
		skybox.texture(sky)

		#texture mapping for broom
		self.woodTex = viz.addTexture('woodtex.jpg')
		self.broom.texture(self.woodTex)

		#score message displayed on the screen
		self.text = viz.addText("Score: " + str(self.catches), viz.SCREEN, pos=[0.01,0.92,0])
		self.text.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM)
		self.text.color(0.95,0.95,0.95)

		
		#lighting
		self.mylight=viz.addLight()
		self.mylight.enable()
		self.mylight.color(1,1,1)
		mat = viz.Matrix()
		mat.postAxisAngle(1,0,0, 110)
		self.mylight.setMatrix(mat)
		#viz.MainView.getHeadLight().disable()
		self.snitch.specular([1,1,.9])
		
		
		#choose a snitch path
		pathNum = random.randint(0,3)
		self.snitchPath(pathNum)
		
		#collision detection
		self.broom.collideSphere(radius=10)
		self.broom.disable( viz.DYNAMICS )
		self.snitch.collideMesh()
		self.snitch.disable( viz.DYNAMICS )
		self.snitch.enable(viz.COLLIDE_NOTIFY)
		self.callback(viz.COLLIDE_BEGIN_EVENT, self.onCollideBegin)
		
		viz.playSound('Harry_Potter_Theme.wav')
		
#increase number of catches when collision occurs
	def onCollideBegin(self, e):
		self.catches += 1
		viz.playSound('ball_sound.wav')
		#print("catches: " + str(self.catches))
	
	
	# Key pressed down event code.
	def onKeyDown(self,key):
		if (key == viz.KEY_RIGHT):
			self.dtheta = 2
		if (key == viz.KEY_LEFT):
			self.dtheta = -2
		if (key == viz.KEY_DOWN):
			self.dalpha = 2
		if (key == viz.KEY_UP):
			self.dalpha = -2
		if (key == ' '):
			self.moving = True
	
	def onKeyUp(self, key):
		#stop moving broom
		if (key == ' '):
			self.moving = False
		if (key == viz.KEY_RIGHT or key == viz.KEY_LEFT):
			self.dtheta = 0
		if (key == viz.KEY_DOWN or key == viz.KEY_UP):
			self.dalpha = 0
			
	def onTimer(self,num):
		self.alpha += self.dalpha
		self.theta += self.dtheta
		if (self.moving):
			self.x = self.x +  .75*math.sin(math.radians(self.theta))*math.cos(math.radians(self.alpha))  
			self.z = self.z + .75*math.cos(math.radians(self.theta))*math.cos(math.radians(self.alpha))
			self.y = self.y + .75*math.sin(math.radians(-self.alpha))
		self.transform()
		
		#Displays on the screen the score that the player scores by catching the snitch
		m = viz.Matrix()
		m.postTrans(-100,-100,0)
		self.text.setMatrix(m)
		#self.text2D.message("Score: " + str(self.catches))
		self.text = viz.addText("Score: " + str(self.catches), viz.SCREEN, pos=[0.01,0.92,0])
		self.text.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM)
		self.text.color(0.95,0.95,0.95)
		
		
	def transform(self):
		#transform broom
		m=viz.Matrix()
		#m.postScale(.005, .005, .005)
		m.postAxisAngle(1,0,0,90) #extra for cylinder
		m.postAxisAngle(1,0,0,self.alpha)
		m.postAxisAngle(0,1,0,self.theta)
		m.postTrans(self.x, self.y, self.z)
		#self.broom.getNode().setMatrix(m)
		self.broom.setMatrix(m)
		
		#transform view
		dx =  0.5*(math.sin( math.radians( self.theta ) ))
		dz =  0.5*(math.cos( math.radians( self.theta ) ))
		dy =  0.5*(math.sin(math.radians(-self.alpha)))
		view = viz.MainView
		mat = viz.Matrix()
		mat.postTrans(0,0.75,0);
		mat.postAxisAngle(1,0,0,self.alpha)
		mat.postAxisAngle(0,1,0,self.theta)
		mat.postTrans(self.x-dx,self.y-dy,self.z-dz)
		view.setMatrix(mat)	
		
	def snitchPath(self, pathNum):
		#Add the path. 
		self.path = viz.addAnimationPath()

		#Add control points to the path, along with their time stamp.

		if (pathNum < 4):
			self.path.addControlPoint(0,pos=(22,31,20),euler=(90,0,0))
			self.path.addControlPoint(3,pos=(-22,21,26),euler=(0,90,0))
			self.path.addControlPoint(5,pos=(-22,41,46),euler=(0,0,90))
			self.path.addControlPoint(6.5,pos=(-10,10,60),euler=(90,0,0))
			self.path.addControlPoint(8,pos=(12,21,26),euler=(0,90,0))
			self.path.addControlPoint(10,pos=(42,45,50),euler=(0,0,90))
			self.path.addControlPoint(11.5,pos=(17,35,25),euler=(0,90,0))
			self.path.addControlPoint(12,pos=(22,31,20),euler=(90,0,0))
		else: 
			pass
			
		
		#Loop the path to loop back to replay from beginning
		self.path.setLoopMode(viz.LOOP)
		self.path.computeTangents()
		self.path.setTranslateMode(viz.CUBIC_BEZIER)
		
		#Link the model to a path.
		self.link = viz.link(self.path,self.snitch)

		#Play the path.
		self.path.play()
