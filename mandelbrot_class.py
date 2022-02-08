import matplotlib.pyplot as plt

from numpy import linspace


class Mandelbrot:
    def __init__(self,n):
            self.plane = self.createPlane(n)
    
    def createPlane(self,n):
        '''Creates 2D plane of diverging points.'''
        z0 = complex(0.,0.)
        #reAx = linspace(-2,0.5,n)
        reAx = linspace(-3,1.5,n)
        imAx = linspace(-2.25,2.25,n)
        zAx = reAx + 1.j * imAx[:,None]
        plane = [ [self.divergingPoint(z0, point) for point in row] for row in zAx]
        return plane
    
    def divergingPoint(self,z,c):
        '''Determines the iteration where point starts diverging.'''
        maxIter = 60
        iteration = 0
        while (abs(z) <= 2 and iteration < maxIter):
            z = self.seed(z,c)
            iteration += 1
        return iteration
    
    def seed(self,z,c):
        return z * z + c
    
    def createPlot(self,**kwargs):
        fig,ax = plt.subplots()
        ax.imshow(self.plane,**kwargs)
        ax.set_xticks([])
        ax.set_yticks([])
        fig.tight_layout()
        self.fig = fig
    
    def savePlot(self,**kwargs):
        self.fig.savefig(**kwargs)


if __name__ == '__main__':
    M = Mandelbrot(1000)
    M.createPlot(cmap='twilight_shifted_r')
    M.savePlot(fname='/Users/ja4garci/Documents/PythonFiles/projects2022/mandel.png',
               dpi=300)
    

