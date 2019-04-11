#quidditch.py

import viz
import vizshape
import vizcam
import math
import os

from Model import *


class quidditch(viz.EventClass):
	def __init__(self):
		
		#rotate view
		#self.view=viz.MainView
		#mat = viz.Matrix()
		#mat.postAxisAngle(1,0,0,90)
		#mat.postTrans(0,20,50)
		#self.view.setMatrix(mat)
		
		viz.EventClass.__init__(self)
		
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown)
		self.callback(viz.KEYUP_EVENT, self.onKeyUp)
		self.callback(viz.TIMER_EVENT,self.onTimer)
		self.starttimer(1,1.0/25.0,viz.FOREVER)
		
		
		# avatar's x,z location in space and its rotation angle
		self.theta = -90
		self.alpha = 0
		self.x = 10
		self.z = 45
		self.y = 20
		self.dtheta = 0
		self.dalpha = 0
		self.moving = False
		
		
		self.quadribol = Model('quadribol'+os.sep+'model.osgb')
		#self.snitch = Model('snitch'+os.sep+'scene.gltf')
		self.broom = Model('broom'+os.sep+'source'+os.sep+'broom.obj')
		
		#woodTexture = viz.addTexture('wood.jpeg')
		#self.broom.texture(woodtexture)
		
		#rescale snitch and move into place, doesnt animate as of now
		#self.snitch.setScale(.001)
		#self.snitch.setLocation(self.snitch.getX(),self.snitch.getY()+15,self.snitch.getZ()+50)
		
		self.broom.setScale(.005)
		self.broom.setLocation(self.broom.getX()+10,self.broom.getY()+15,self.broom.getZ()+40)
		
		self.mount = viz.addTexture('mountainTexture.png')
		self.mount.wrap(viz.WRAP_S,viz.REPEAT)
		self.mount.wrap(viz.WRAP_T,viz.REPEAT)
		
		
		#texture mapping on sky cube for background
		sky = viz.add(viz.ENVIRONMENT_MAP,'sky.jpg')

		skybox = viz.add('skydome.dlc')
		skybox.texture(sky)
		
		cube= viz.addTexQuad()
		#quad.setPosition([-.75,2,3])
		#quad.texture(self.mount)
		
	# Key pressed down event code.
	def onKeyDown(self,key):
		if (key == viz.KEY_RIGHT):
			self.dtheta = 5
		if (key == viz.KEY_LEFT):
			self.dtheta = -5
		if (key == viz.KEY_DOWN):
			self.dalpha = 5
		if (key == viz.KEY_UP):
			self.dalpha = -5
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
			self.x = self.x + math.sin(math.radians(self.theta))
			self.z = self.z + math.cos(math.radians(self.theta))
			self.y = self.y - math.sin(math.radians(self.alpha))
		self.transform()
			
	def transform(self):
		m=viz.Matrix()
		m.postScale(.005, .005, .005)
		m.postAxisAngle(1,0,0,self.alpha)
		m.postAxisAngle(0,1,0,self.theta)
		m.postTrans(self.x, self.y, self.z)
		self.broom.getNode().setMatrix(m)
		
		dx =  3.0*(math.sin( math.radians( self.theta ) ))
		dz =  3.0*(math.cos( math.radians( self.theta ) ))
		dy =  (math.sin(math.radians(self.alpha)))
		view = viz.MainView
		mat = viz.Matrix()
		mat.postAxisAngle(1,0,0,self.alpha)
		mat.postAxisAngle(0,1,0,self.theta)
		mat.postTrans(self.x-dx,self.y+dy,self.z-dz)
		view.setMatrix(mat)	
		



		
		
	
		