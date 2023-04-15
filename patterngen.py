#!/usr/bin/env python
"""Python SVG Pattern Generator"""
print(__doc__)

import random



class Shape:
    def __init__(self) -> None:
        pass



class Circle(Shape):
    """Circle class
    """
    def __init__(self, cir: tuple, col: tuple) -> None:
        """
        Generates a Circle with values (cx, cy, rad) 
        and colour and opacity (red, green, blue, op) 
        """
        self.cx: int    = cir[0]    # center x point
        self.cy: int    = cir[1]    # center y point
        self.rad: int   = cir[2]    # radius
        self.red: int   = col[0]
        self.green: int = col[1]
        self.blue: int  = col[2]
        self.op: float  = col[3]
    
    def __str__(self) -> str:
        return f'Circle(({self.cx},{self.cy},{self.rad}), ({self.red},{self.green},{self.blue},{self.op:.1f}))'

    def getXY(self) -> tuple:
        return (self.cx, self.cy)

    def getRad(self) -> int:
        return self.rad
    
    def getRGB(self) -> tuple:
        return (self.red, self.green, self.blue)
        
    def draw(self, f: IO[str], t: int) -> None:
        """draw method
        Draws a cirle into file f with t tabs
        """
        ts: str = "   " * t
        line1: str = f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.rad}" '
        line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></circle>'
        f.write(f"{ts}{line1+line2}\n")



class Rectangle(Shape):
    """Rectangle class
    """
    def __init__(self, rec: tuple, col: tuple) -> None:
        """
        Generates Rectangle with values (tlx, tly, w, h)
        and colour and opacity (red, green, blue, op)
        """
        self.tlx: int   = rec[0]    # top left x point
        self.tly: int   = rec[1]    # top left y point
        self.w: int     = rec[2]    # width 
        self.h: int     = rec[3]    # height 
        self.red: int   = col[0]
        self.green: int = col[1]
        self.blue: int  = col[2]
        self.op: float  = col[3]
    
    def __str__(self) -> str:
        return f'Rectangle(({self.tlx},{self.tly},{self.w},{self.h}), ({self.red},{self.green},{self.blue},{self.op:.1f}))'

    def getXY(self) -> tuple:
        return (self.tlx, self.tly)

    def getWH(self) -> tuple:
        return (self.w, self.h)
    
    def getRGB(self) -> tuple:
        return (self.red, self.green, self.blue)
    
    def draw(self, f: IO[str], t: int) -> None:
        """draw"""
        ts: str = "   " * t
        line1: str = f'<rect x="{self.tlx}" y="{self.tly}" width="{self.w}" height="{self.h}" '
        line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></rect>'
        f.write(f"{ts}{line1+line2}\n")



class GenRandom:
    """GenRandom class
    """
    def __init__(self, lo: int=0, hi: int=0) -> None:
        """
        Generates a GenRandom from ranges lo to hi
        """
        if (lo == 0 and hi == 0):
            self.rnum: float = random.random() # random float from 0.0 to 1.0
        else:
            self.rnum: float = random.randint(lo, hi) # random int between lo and hi (inclusive)



class ArtConfig:
    """ArtConfig class
    """
    def __init__(self, sha:tuple=(0,1), xy:tuple=(500,300), rad:tuple=(0,100), w:tuple=(10, 100), h:tuple=(10,100), rgb:tuple=(255,255,255)) -> None:
        """
        Creates random values for a shape 
        within specified ranges as parameters
        """
        self.sha: int = GenRandom(sha[0],sha[1]).rnum // 1
        self.x: int = GenRandom(0,xy[0]).rnum
        self.y: int = GenRandom(0,xy[1]).rnum
        self.rad: int = GenRandom(rad[0],rad[1]).rnum
        self.w: int = GenRandom(w[0],w[1]).rnum
        self.h: int = GenRandom(h[0],h[1]).rnum
        self.r: int = GenRandom(0,rgb[0]).rnum
        self.g: int = GenRandom(0,rgb[1]).rnum
        self.b: int = GenRandom(0,rgb[2]).rnum
        self.op: float = GenRandom().rnum
    
    def __str__(self) -> str:
        return (f'{self.sha:>4} {self.x:>4} {self.y:>4} {self.rad:>4} {self.rx:>4} {self.ry:>4} {self.w:>4} {self.h:>4} {self.r:>4} {self.g:>4} {self.b:>4} {self.op:>4.3f}')
    
    def createShape(self) -> Shape:
        """createShape"""
        if (self.sha == 0):
            return Circle((self.x,self.y,self.rad), (self.r,self.g,self.b,self.op))
        else:
            return Rectangle((self.x,self.y,self.w,self.h),(self.r,self.g,self.b,self.op))



class ProEpilogue:
    """ProEpilogue class
    """
    def __init__(self, title: str) -> None:
        """
        Generates Prologue and Epilogue text
        with specified title
        """
        self.prologue: str = f"<html>\n<head>\n   <title>{title}</title>\n<head>\n<body>"
        self.epilogue: str = f"</body>\n</html>"
    
    def writePro(self, f: IO[str]) -> None:
        """writePro method"""
        f.write(self.prologue)
    
    def writeEpi(self, f: IO[str]) -> None:
        """writeEpi method"""
        f.write(self.epilogue)




def openSVGcanvas(f: IO[str], t: int, canvas: tuple) -> None:
    """openSVGcanvas method"""
    ts: str = "   " * t
    writeHTMLcomment(f, t, "Define SVG drawing box")
    f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

def closeSVGcanvas(f: IO[str], t: int) -> None:
    """closeSVGcanvas method"""
    ts: str = "   " * t
    f.write(f"{ts}</svg>\n")

def writeHTMLline(f: IO[str], t: int, line: str) -> None:
    """writeLineHTML method"""
    ts = "   " * t
    f.write(f"{ts}{line}\n")
    
def writeHTMLcomment(f: IO[str], t: int, com: str) -> None:
    """writeHTMLcomment method"""
    ts: str = "   " * t
    f.write(f"{ts}<!--{com}-->\n")

def createCard(f: IO[str], num:int, frame:tuple, shapes:tuple, rad:tuple, w:tuple, h:tuple, rgb:tuple=(255,255,255)) -> None:
    """createCard"""
    for i in range(num):
        conf:ArtConfig = ArtConfig(shapes,frame,rad,w,h,rgb)
        shp: Shape = conf.createShape()
        if type(shp) is Rectangle:
            shp.draw(f,2)
        if type(shp) is Circle:
            shp.draw(f,2)



def main():
    """main"""
    # Setting up HTML page
    pelogue: ProEpilogue = ProEpilogue("My Art")
    f: IO[str] = open("patterns.html", "w")
    pelogue.writePro(f)

    # FRAME 1
    # Mainly Red
    # Utilises both Circles and Rectangles
    frame1:tuple = (1300, 500)  # (width, height) of image
    openSVGcanvas(f,1, frame1)
    createCard(f, 300, frame1, (0,1), (20,200), (10, 30), (50, 200), (255,5,50))
    closeSVGcanvas(f,1)

    # FRAME 2
    # Mostly Blue
    # Utilises ONLY Circles
    frame2:tuple = (1000, 500)  # (width, height) of image
    openSVGcanvas(f,1, frame2)
    createCard(f, 50, frame2, (0,0), (50,100), (100, 300), (20, 50), (100,10,255))
    closeSVGcanvas(f,1)

    # FRAME 3
    # Mostly Green
    # Utilises ONLY Rectangles
    frame3:tuple = (300,500)    # (width, height) of image
    openSVGcanvas(f,1, frame3)
    createCard(f, 100, frame3, (1,1), (50,100), (50, 100), (50, 100), (10,255,100))
    closeSVGcanvas(f,1)

    pelogue.writeEpi(f)


if __name__ == "__main__":
    main()
