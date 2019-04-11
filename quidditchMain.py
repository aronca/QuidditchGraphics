#quidditchMain.py

import viz
import vizshape
from quidditch import *


# set size (in pixels) and title of application window
viz.window.setSize( 640*1.5, 480*1.5 )
viz.window.setName( "Quidditch Practice" )

# get graphics window

window = viz.MainWindow
# setup viewing volume

# set background color of window to black 
viz.MainWindow.clearcolor( [0,0,0] ) 

# allows mouse to rotate, translate, and zoom in/out on object
pivotNav = vizcam.PivotNavigate()

c = quidditch()

# render the scene in the window
viz.go()













viz.go()