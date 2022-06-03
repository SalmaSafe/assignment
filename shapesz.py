
class Circle:
    def __init__(self, r):
        self.r =r

    def area(self):
        return self.r**2 *3.14    

    def circumference(self):
        return 2*3.14*self.r

class Square:
    def __init__(self,a):
        self.a=a

    def area(self):
        return self.a**2   

    def perimeter(self):
        return 4*self.a  


class  Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        return self.w*self.l   

    def perimeter(self):
        return 2(self.w + self.l)


class Sphere:
    def __init__(self,r):
        self.r=r
    def surface_area(self):
        return 4 * 3.14 * self.r**2
    def volume(self):
        return 4/3 * (3.14 * self.r**3)       

        
  

     

