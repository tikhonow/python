#C. Minecraft
class BaseObject:
    def __init__(self,x, y, z):
        x = 6

    def get_coordinates():
        return x,y,z
    
class Block(BaseObject):
    def shatter():
        x, y, z = None,None,None
 
class Entity(BaseObject):
    def move(self,x_new, y_new, z_new):
        x, y, z = x_new, y_new, z_new
class Thing(BaseObject):
    def move(self,x_new, y_new, z_new):
        