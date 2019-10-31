import pyglet
from plot import plotMandelbrot

WIDTH = 600
HEIGHT = 600
MAX_ITER = 160

class BoundsRect:
        def __init__(self, x, y, length):
                self.set(x, y, length)
                self._visible = False
                
        def setVisible(self, isVisible):
                self._visible = isVisible
                
        def draw(self):
                if(self._visible):
                        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, self._lineloop)
        
        def set(self, x=None, y=None, length=None):
                self._x = self._x if x is None else x
                self._y = self._y if y is None else y
                self._length = self._length if length is None else length
                self._lineloop = ('v2f', (self._x, self._y,
                                          self._x + self._length, self._y,
                                          self._x + self._length, self._y + self._length,
                                          self._x, self._y + self._length))
                
                

window = pyglet.window.Window()
window.set_size(WIDTH,HEIGHT)

# ([x1, x2],[y1, y2])
curBounds = BoundsRect(-1.0, -1.0, 2.0)
newBounds = BoundsRect(-1.0, -1.0, 2.0)
plotMandelbrot(curBounds._x, curBounds._x + curBounds._length, curBounds._y, curBounds._y + curBounds._length, WIDTH, HEIGHT, MAX_ITER, 1)
mandelbrotPic = pyglet.image.load("output.png")

@window.event  
def on_mouse_press(x, y, button, modifiers):
        newBounds.set(x=x, y=y)

@window.event  
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        xChng = x- newBounds._x
        yChng = y- newBounds._y
        newLength = xChng if xChng > yChng else yChng
        newBounds.set(length=newLength)
        newBounds.setVisible(True)
        
@window.event
def on_mouse_release(x, y, button, modifiers):
        newBounds.setVisible(False)
        xNorm = newBounds._x / WIDTH
        yNorm = newBounds._y / HEIGHT
        lenNorm = newBounds._length / WIDTH
        newX = curBounds._x + (xNorm * curBounds._length)
        newY = curBounds._y + (yNorm * curBounds._length)
        newLen = lenNorm * curBounds._length
        
        curBounds.set(newX, newY, newLen)
        print(str(xNorm) + " " + str(yNorm) + " " + str(lenNorm))
        print(str(curBounds._x) + " " + str(curBounds._y) + " " + str(curBounds._length))
        plotMandelbrot(curBounds._x, curBounds._x + curBounds._length, curBounds._y, curBounds._y + curBounds._length, WIDTH, HEIGHT, MAX_ITER, 1)
        
        

@window.event
def on_draw():
        window.clear()
        mandelbrotPic = pyglet.image.load("output.png")
        mandelbrotPic.blit(0,0)
        newBounds.draw()

pyglet.app.run()


