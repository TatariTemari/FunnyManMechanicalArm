# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 22:38:07 2022

@author: Dr. Robel Geressu
"""

import numpy as np
import matplotlib.pyplot as plt

def exercise_1():
    length1 = 1
    length2 = 0.6
    
    # experiment by changing the angels below
    angle1InDegrees = 30
    angle2InDegrees = 90
    
    angle1InRadians = np.deg2rad(angle1InDegrees)
    angle2InRadians = np.deg2rad(angle2InDegrees)
    
    ''' lets check the values in radians'''
    
    print ('angle1InRadians',angle1InRadians)
    print ('angle2InRadians',angle2InRadians)
    
    ''' we will fix one of the lines at the origin x,y = 0,0'''
    x0 = 0
    y0 = 0
    
    x1 = length1*np.cos(angle1InRadians)
    y1 = length1*np.sin(angle1InRadians)
    
    # plt.plot([x0,x1],[y0,y1],color = 'b')
    
    x2 = length2*np.cos(angle2InRadians)
    y2 = length2*np.sin(angle2InRadians)
    
    x3 = x1 + x2
    y3 = y1 + y2
    
    fig,ax = plt.subplots()
    

    ax.plot([x0,x1],[y0,y1],color = 'blue')
    # ax.plot([x0,x2],[y0,y2],color = 'grey')
    # ax.plot([x1,x2],[y1,y2],color = 'red')
    # ax.plot([x2,x3],[y2,y3],color = 'magenta')
    
    # lets make the following line differnt by adding more attributes
    # remember you can change the values (e.g., the line width, line type and transparency)
    # you can always get a great tip on how to change various elements on google
    ax.plot([x1,x3],[y1,y3],color = 'green', linewidth = 3, linestyle = '--', alpha = 0.5)
    
    
    '''we can mark the joints with markers'''
    ax.scatter([x0,x1],[y0,y1],marker = 'o',color = 'blue')
    ax.scatter([x1,x3],[y1,y3],marker = '*',color = 'red')
    
def exercise_2():
    length1 = 1
    length2 = 0.6
    ''' we will change the angles iteratively with a for loop'''
    
    angle1InDegrees = 30
    angle2InDegrees = 90
    for i in range(50):
        # experiment with the increment (e.g., try 1, 5, 10)
        # also try different sizes for the increments of the two angles
        # you can also change the number of iterations in the for loop
        
        # you will see the difference in the plots on the right side of your screen
        # if you are using the 'Spyder' debugger. Open the Plots pane 
        # on the top right hand side
        angle1InDegrees = angle1InDegrees + 10
        angle2InDegrees = angle2InDegrees + 2
        
        angle1InRadians = np.deg2rad(angle1InDegrees)
        angle2InRadians = np.deg2rad(angle2InDegrees)
        
    
        
        ''' we will fix one of the lines at the origin x,y = 0,0'''
        x0 = 0
        y0 = 0
        
        x1 = length1*np.cos(angle1InRadians)
        y1 = length1*np.sin(angle1InRadians)
        
        # plt.plot([x0,x1],[y0,y1],color = 'b')
        
        x2 = length2*np.cos(angle2InRadians)
        y2 = length2*np.sin(angle2InRadians)
        
        x3 = x1 + x2
        y3 = y1 + y2
        
        fig,ax = plt.subplots()
        
    
        ax.plot([x0,x1],[y0,y1],color = 'blue', linewidth = 6, linestyle = ':', alpha = 0.8)
        # ax.plot([x0,x2],[y0,y2],color = 'grey')
        # ax.plot([x1,x2],[y1,y2],color = 'red')
        # ax.plot([x2,x3],[y2,y3],color = 'magenta')
        ax.plot([x1,x3],[y1,y3],color = 'green', linewidth = 3, linestyle = '--', alpha = 0.5)
        '''we can mark the joints with markers'''
        ax.scatter([x0,x1],[y0,y1],marker = 'o',color = 'blue')
        ax.scatter([x1,x3],[y1,y3],marker = '*',color = 'red')
        
        # we are fixing the minimu and maximum values that will be shown in the plot window
        # below, otherwise there will be an optical illusion where the size of the
        # arms (length of lines)  seem to change size
        plt.xlim([-2,2])
        plt.ylim([-0.1,2])
        
# the computer program will start from the following line
# it will then excute the codes below it (which have to be indented)
if __name__ == "__main__":
    
    # uncomment only one of the following to run the code in side the functions
    # I would recommend that you try to type  the code in the function into a new script
    # exercise_1()
    exercise_2()
