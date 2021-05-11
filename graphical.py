# ------------------------------------------------------ #
# Description: functions file to generate graphical renditions
# of NewtEotWash QLM primitives. 
# By: Parker Lamb
# Mentor: Dr. Svenja Fleischer
# ------------------------------------------------------ #
import matplotlib.pyplot as plt

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

# !! Note - each primitive is a function of x,y and z. Make each function return OrderedDict of (x,y,z), so translation and rotation
# functions can modify them directly.

# === BEGIN GEOMETRICAL PRIMITIVES === #
def rect_prism(x,y,z,ax):
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
    ax : Axes3D
        Plot object returned from setup()
    Returns
    -------
    None
    """
    return

def tri_prism(h,d,y1,y2,ax):
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
    ax : Axes3D
        Plot object returned from setup()
    Returns
    ------
    None
    """
    return

def annulus(H,Ri,Ro,phic,phih,ax):
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
    ax : Axes3D
        Plot object returned from setup()
    Returns
    ------
    None
    """
    return

def cone(h,r1,r2,ax):
    """
    Description: adds a cone to the 3D plot
    Inputs
    ------
    h : float
        Total height along z axis. Centered about z=0.
    r1 : float
        Radius of upper section of cone
    r2 : float
        Radius of lower section of cone
    ax : Axes3D
        Plot object returned from setup()
    Returns
    ------
    None
    """
    return

# === BEGIN TRANSLATION FUNCTIONS === #

# === BEGIN ROTATION PRIMITIVES === #
