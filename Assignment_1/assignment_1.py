# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:37:42 2019

@author: gordon.garisch

Description:
    Code for assignment 1.
    Group is "Accenture Assemble"
    Members:
        B Crowe
        G Garisch
        J Troianello
        C Stipcak
"""

# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Create values for x axis
X = np.linspace(0, 2*np.pi, 360)

# Create plots
plt.cla()                               #Remove existing plots
plt.plot(X, np.cos(X))                  #Plot for cosine
plt.plot(X, np.sin(X))                  #Plot for sine
plt.legend(('cosine', 'sine'))          #Add legend
plt.xlabel('Angle in Rad')              #Add x label
plt.ylabel('Function Value')            #Add y label
plt.title('Trigonometric Functions')    #Add title
plt.show()                              #Show plot
