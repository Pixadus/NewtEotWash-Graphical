# ------------------------------------------------------ #
# Description: functions file to generate graphical renditions
# of NewtEotWash QLM primitives. 
# By: Parker Lamb
# Mentor: Dr. Svenja Fleischer
# ------------------------------------------------------ #
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict

# TODO: Add r1 to cone

def setup():
    """
    Description: sets the 3D environment up, and makes it
    accessible to adding primitives. 
    Inputs
    ------
    None
    Returns
    ------
    ax : Plot (Axes3D)
        A modifiable plot to display primitives defined below.
    Documentation: https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html
    """
    fig = plt.figure()
    plot = fig.add_subplot(111, projection="3d")
    return(plot)

def display(shapes):
    """
    Description: adds all shapes to the plot and displays it.. 
    Inputs
    ------
    shapes : List
        List of shapes to add to the plot. 
    y : float
        Total width along y axis. Centered about y=0.
    z : float
        Total height along z axis. Centered about z=0.
    Returns
    -------
    np.array(xs,ys,zs)
    """

# !! Note - each primitive is a function of x,y and z. Make each function return OrderedDict of (x,y,z), so translation and rotation
# functions can modify them directly.

# === BEGIN GEOMETRICAL PRIMITIVES === #
def rect_prism(x,y,z):
    """
    Description: adds a rectangular prism to the 3D plot. 
    Inputs
    ------
    x : float
        Total length along x axis. Centered about x=0.
    y : float
        Total width along y axis. Centered about y=0.
    z : float
        Total height along z axis. Centered about z=0.
    Returns
    -------
    np.array(xs,ys,zs)
    """
    return

def tri_prism(h,d,y1,y2):
    """
    Description: adds a triangular prism to the 3D plot. 
    Inputs
    ------
    h : float
        Total height along z axis. Centered about z=0.
    d : float
        Length along x axis.
    y1 : float
        Position of first vertex along y-axis
    y2 : float
        Position of second vertex along y-axis
    Returns
    ------
    np.array(xs,ys,zs)
    """
    return

def annulus(H,Ri,Ro,phic,phih):
    """
    Description: adds a cylindrical annulus to the 3D plot.
    Inputs
    ------
    H : float
        Total height along z axis. Centered about z=0.
    Ri : float
        Inner radius of annulus
    Ro : float
        Outer radius of annulus
    phic : float
        Central angle of annular section, in radians
    phih : float
        Half angular width of annular section, in radians
    Returns
    ------
    np.array(xs,ys,zs)
    """
    return

def cone(h,r2):
    """
    Description: adds a cone to the 3D plot
    Inputs
    ------
    h : float
        Total height along z axis. Centered about z=0.
    r1 : float
        Radius of upper section of cone
    r2 : float
        Radius of base of cone
    Returns
    ------
    np.array(xs,ys,zs)
    """
    n = 64 # Number of surfaces. More is more detail, but longer time to run
    xs = np.linspace(-r2, r2, n)
    ys = np.linspace(-r2, r2, n)
    zs = np.array([max(h * (1 - np.hypot(x, y) / r2), 0)
               for x in xs for y in ys]).reshape((n, n))
    mxs, mys = np.meshgrid(xs, ys)
    return(np.array([mxs,mys,zs]))

# === BEGIN TRANSLATION FUNCTIONS === #
def translate(shape,trans):
    """
    Description: translates a shape
    Inputs
    ------
    shape : np.array
        Shape defined in terms of x, y, z coordinates.
    trans : np.array
        Translation array defined in terms of +x,+y, +z coordinates.
    Returns
    ------
    np.array(xs+x,ys+y,zs+z)
    """
    # We hardly need a function for this, but it will keep consistency with translation_qlm().
    translated_array = shape+trans
    return(translated_array)

# === BEGIN ROTATION PRIMITIVES === #
