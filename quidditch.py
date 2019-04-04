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
		
		self.quadribol = Model('quadribol'+os.sep+'model.dae')
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
		self.mount.wrap(viz.WRAP_S,viz.REPEAT)
		self.mount.wrap(viz.WRAP_T,viz.REPEAT)
		
		
		
		sky = viz.add(viz.ENVIRONMENT_MAP,'sky.jpg')

		skybox = viz.add('skydome.dlc')
		skybox.texture(sky)
		
		
		

		#mount texture coords
		cube= viz.addTexQuad()
		quad.setPosition([-.75,2,3])
		quad.texture(self.mount)
		
		
	
		