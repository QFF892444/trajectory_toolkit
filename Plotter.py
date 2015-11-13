from pylab import *
import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    td = []
    colIDs = []
    lines = []
    axes = []
    subplotDim = [1,1]
    figureId = 0
    maxPoints = 1000;
    
    def __init__(self, figureId, subplotDim, isLive=False, maxPoints=1000):
        self.figureId = figureId
        self.maxPoints = maxPoints
        self.subplotDim = subplotDim
        # Open Plot when live plotting
        if isLive:
            figure(self.figureId)
            plt.ion()            
            plt.show();
    
    def addDataToSubplot(self, td, colID, plotID, color, name):
        self.colIDs.append(colID);
        self.td.append(td)
        # Add lines to subplot
        figure(self.figureId)
        axis = subplot(self.subplotDim[0], self.subplotDim[1], plotID)
        self.axes.append(axis);
        self.lines.append(axis.plot([], [], c=color, label=name)[0])
        plt.legend()

    def refresh(self):
        figure(self.figureId)
        for i in xrange(0,len(self.colIDs)):
            # Subsample Data
            stepSize = floor(self.td[i].end()/self.maxPoints)+1;
            self.lines[i].set_xdata(self.td[i].col(0)[1::stepSize])
            self.lines[i].set_ydata(self.td[i].col(self.colIDs[i])[1::stepSize])
        # Update axis limits
        for axis in self.axes:
            axis.relim()
            axis.autoscale_view(True,True,True)
        # Redraw Plot
        plt.draw();
        
    def show(self):
        # Refresh and show plot
        plt.ioff();            
        self.refresh();
        plt.show();