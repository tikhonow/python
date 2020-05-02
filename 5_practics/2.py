#C. Minecraft
class BaseObject:
    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates():
        return self.x, self.y, self.z
    
class Block(BaseObject):
    def shatter():
        self.x, self.y, self.z = None,None,None
 
class Entity(BaseObject):
    def move(self,x_new, y_new, z_new):
        self.x, self.y, self.z = x_new, y_new, z_new
class Thing(BaseObject):
    pass