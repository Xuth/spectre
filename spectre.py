import turtle
from intervaltree2d import IT2D, IT2DNode

class SegmentStore:
    def __init__(self, sigma=0.01):
        self.segments = IT2D()
        self.sigma = sigma  #if points differ by sigma or less on both axes they are considered the same

    def insert(self, x1, y1, x2, y2, sweep):
        # canonicalize the order of the points based on sweep
        if sweep:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        maybeMatches = self.segments.findIntersectPoint(x1, y1)


        # check maybeMatches
        s = self.sigma
        for mm in maybeMatches:
            if (abs(mm[2]-x2) < s) and (abs(mm[3]-y2) < s):
                print(f"{x1},{y1} {x2},{y2} is a duplicate")
                return

        self.segments.insert(IT2DNode(x1-s, x1+s, y1-s, y1+s, (x1, y1, x2, y2)))
        #print(f"{x1},{y1} {x2},{y2} inserted")

    def allSegments(self):
        return self.segments.all()
            
            
def writeSVG(name):
    with open(name, "w") as f:
        f.write('<svg width="300mm" height="300mm" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">\n')

        for seg in segments.allSegments():
            print (repr(seg))
            x1, y1, x2, y2 = seg
            y1 = 300 - y1
            y2 = 300 - y2
            #f.write(f'  <path d="M {x1} {y1} A 7 7 0 0 0 {x2} {y2}" stroke="black" fill="none" stroke-wideth="0.2"/>\n')
            f.write(f'  <path d="M {x1} {y1} A 7 7 0 0 1 {x2} {y2}" stroke="black" fill="none" stroke-wideth="0.2"/>\n')
    
        f.write('</svg>\n')
            
def spectre(t, start=0, end=None, size=10):
    def rmp(r, rotate = True):  # rotate, move, print
        sx = round(t.x, 5)
        sy = round(t.y, 5)
        if rotate:
            t.rot(r)
        t.move(size)
        ex = round(t.x, 5)
        ey = round(t.y, 5)
        #print (f'({sx}, {sy}), ({ex}, {ey}), {(i+1)%2}')
        segments.insert(sx, sy, ex, ey, (i+1)%2)
        #print(t)


    directions = [90,  60, -90, 60, 0, 60, 90, -60, 90, -60, 90, 60, -90, 60, # wrap around to continue
                  90, 60, -90, 60, 0, 60, 90, -60, 90, -60, 90, 60, -90, 60]

    if end is None:
        end = start+14
    
    if end <= start:
        end += 14
        
    first = True
    for i in range(start,end):
        if first:
            rmp(directions[i], rotate = False)
            first = False
        else:
            rmp(directions[i])
    

segments = SegmentStore()


t = turtle.Turtle()
t.moveAbs(100,100)
t.rotAbs(0)
spectre(t)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=6)
t.rot(180)
spectre(t, start=4)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=7)
t.rot(180)
spectre(t, start=5)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=10)
t.rot(180)
spectre(t, start=4)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=13)
t.rot(180)
spectre(t, start=5)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=6)
t.rot(180)
spectre(t, start=4, end=12)
t.rot(180)
spectre(t, start=10)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=6)
t.rot(180)
spectre(t, start=4, end=12)
t.rot(180)
spectre(t, start=10, end=2)
t.rot(180)
spectre(t, start=10)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=6)
t.rot(180)
spectre(t, start=4, end=12)
t.rot(180)
spectre(t, start=10, end=5)
t.rot(180)
spectre(t, start=13)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=7)
t.rot(180)
spectre(t, start=5, end=11)
t.rot(180)
spectre(t, start=9)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=13)
t.rot(180)
spectre(t, start=5, end=12)
t.rot(180)
spectre(t, start=10)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=10)
t.rot(180)
spectre(t, start=4, end=11)
t.rot(180)
spectre(t, start=7)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=10)
t.rot(180)
spectre(t, start=4, end=11)
t.rot(180)
spectre(t, start=7, end=2)
t.rot(180)
spectre(t, start=10)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=10)
t.rot(180)
spectre(t, start=4, end=11)
t.rot(180)
spectre(t, start=7, end=0)
t.rot(180)
spectre(t, start=2)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=10)
t.rot(180)
spectre(t, start=4, end=11)
t.rot(180)
spectre(t, start=7, end=11)
t.rot(180)
spectre(t, start=7)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=10)
t.rot(180)
spectre(t, start=4, end=11)
t.rot(180)
spectre(t, start=7, end=11)
t.rot(180)
spectre(t, start=7, end=1)
t.rot(180)
spectre(t, start=7)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=10)
t.rot(180)
spectre(t, start=4, end=11)
t.rot(180)
spectre(t, start=7, end=11)
t.rot(180)
spectre(t, start=7, end=1)
t.rot(180)
spectre(t, start=7, end=2)
t.rot(180)
spectre(t, start=8)


t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=1)
t.rot(180)
spectre(t, start=7)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=1)
t.rot(180)
spectre(t, start=7, end=12)
t.rot(180)
spectre(t, start=10)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=1)
t.rot(180)
spectre(t, start=7, end=1)
t.rot(180)
spectre(t, start=9)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=1)
t.rot(180)
spectre(t, start=7, end=1)
t.rot(180)
spectre(t, start=9, end=11)
t.rot(180)
spectre(t, start=9)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=14)
t.rot(180)
spectre(t, start=4)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=14)
t.rot(180)
spectre(t, start=4, end=7)
t.rot(180)
spectre(t, start=5)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=14)
t.rot(180)
spectre(t, start=4, end=7)
t.rot(180)
spectre(t, start=5, end=11)
t.rot(180)
spectre(t, start=9)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=14)
t.rot(180)
spectre(t, start=4, end=9)
t.rot(180)
spectre(t, start=5)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=14)
t.rot(180)
spectre(t, start=4, end=9)
t.rot(180)
spectre(t, start=5, end=11)
t.rot(180)
spectre(t, start=7)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=4)
t.rot(180)
spectre(t, start=4)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=4)
t.rot(180)
spectre(t, start=4, end=9)
t.rot(180)
spectre(t, start=5)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=4)
t.rot(180)
spectre(t, start=4, end=11)
t.rot(180)
spectre(t, start=7)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=4)
t.rot(180)
spectre(t, start=4, end=11)
t.rot(180)
spectre(t, start=7, end=1)
t.rot(180)
spectre(t, start=9)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=4)
t.rot(180)
spectre(t, start=4, end=14)
t.rot(180)
spectre(t, start=4)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=4)
t.rot(180)
spectre(t, start=4, end=14)
t.rot(180)
spectre(t, start=4, end=9)
t.rot(180)
spectre(t, start=13)

t.moveAbs(100,100)
t.rotAbs(0)
spectre(t, end=4)
t.rot(180)
spectre(t, start=4, end=14)
t.rot(180)
spectre(t, start=4, end=12)
t.rot(180)
spectre(t, start=0)





writeSVG("spectre_32.svg")



