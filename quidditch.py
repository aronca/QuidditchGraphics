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
		self.view=viz.MainView
		mat = viz.Matrix()
		mat.postAxisAngle(1,0,0,90)
		mat.postTrans(0,20,50)
		self.view.setMatrix(mat)
		viz.EventClass.__init__(self)
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		
		
		# avatar's x,z location in maze and its rotation angle
		self.theta = 0
		self.alpha = 0
		self.x = 10
		self.z = 15
		self.y = 40
		
		self.quadribol = Model('quadribol'+os.sep+'model.osgb')
		#self.snitch = Model('snitch'+os.sep+'scene.gltf')
		self.broom = Model('broom'+os.sep+'source'+os.sep+'broom.obj')
		
		#self.woodTexture = viz.addTexture('wood.jpeg')
		#self.broom.texture(woodtexture)
		
		#rescale snitch and move into place, doesnt animate as of now
		#self.snitch.setScale(.001)
		#self.snitch.setLocation(self.snitch.getX(),self.snitch.getY()+15,self.snitch.getZ()+50)
		
		self.broom.setScale(.005)
		self.broom.setLocation(self.broom.getX()+10,self.broom.getY()+15,self.broom.getZ()+40)
		
		self.mount = viz.addTexture('mountainTexture.png')
		sky = viz.add(viz.ENVIRONMENT_MAP,'sky.jpg')

		skybox = viz.add('skydome.dlc')
		skybox.texture(sky)
		
		#delete this if texture mapping is added
		self.mtn1 = Model('mtn'+os.sep+'model.dae')
		self.mtn2 = Model('mtn'+os.sep+'model.dae')
		self.mtn3 = Model('mtn'+os.sep+'model.dae')
		self.mtn4 = Model('mtn'+os.sep+'model.dae')
		
		
		
		self.mtn1.setScale(2)
		self.mtn1.setLocation(self.mtn1.getX()-60,self.mtn1.getY()-27,self.mtn1.getZ()-26)
		
		
		self.mtn2.setScale(2)
		self.mtn2.setLocation(self.mtn2.getX()-60,self.mtn2.getY()-27,self.mtn2.getZ()+125)
		
		
		self.mtn3.setScale(2)
		self.mtn3.setYRotation(90)
		self.mtn3.setLocation(self.mtn3.getX()-100,self.mtn3.getY()-30,self.mtn3.getZ()+100)
		
		
		self.mtn4.setScale(2)
		self.mtn4.setYRotation(90)
		self.mtn4.setLocation(self.mtn4.getX()+100,self.mtn4.getY()-30,self.mtn4.getZ()+100)
		

		
		
		
		
		#mount texture coords
#		viz.startLayer(viz.QUADS)
#		viz.texCoord(0,1)
#		viz.vertex(-.5,.5,.5)
#		viz.texCoord(1,1)
#		viz.vertex(.5,.5,.5)
#		viz.texCoord(1,0)
#		viz.vertex(.5,-.5,.5)
#		viz.texCoord(0,0)
#		viz.vertex(-.5,-.5,.5)
#		viz.vertices=viz.endLayer()
#		vertices.texture(self.mount)
	
#		
#		s= vizshape.addSphere(radius=50)
#		self.mount.wrap(viz.WRAP_S,viz.REPEAT)
#		self.mount.wrap(viz.WRAP_T,viz.REPEAT)
#		
#		s.texture(self.mount)
		
		
	# Key pressed down event code.
	def onKeyDown(self,key):
		if (key == viz.KEY_RIGHT):
			self.theta = self.theta + 10
		if (key == viz.KEY_LEFT):
			self.theta = self.theta - 10
		if (key == viz.KEY_DOWN):
			self.alpha = self.alpha - 10
		if (key == viz.KEY_UP):
			self.alpha = self.alpha + 10
		if (key == ' '):
			self.x =  self.x + math.sin(math.radians(self.theta))
			self.z = self.z + math.cos(math.radians(self.theta))
			
		
		self.transform()
		
	def transform(self):
		m=viz.Matrix()
		m.postScale(.005, .005, .005)
		m.postAxisAngle(1,0,0,self.alpha)
		m.postAxisAngle(0,1,0,self.theta)
		m.postTrans(self.x, self.y, self.z)
		self.broom.getNode().setMatrix(m)
		
		
		
	
		