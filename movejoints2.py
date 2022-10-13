"""movejoints controller."""


# Step 1: Import the modules.  We'll use 'Robot' to access/control the
# robot and 'numpy' if we want to do any fancy math.
#import numpy as np
from controller import Robot
import math 
#import matplotlib.pyplot as plt 


# Step 2: # Define the devices...
# Create the Robot instance.
robot = Robot()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Extract the two motors.
panmotor  = robot.getDevice('pan')
tiltmotor = robot.getDevice('tilt')

# Also enable the camera (so you can see the video feed).
robot.getDevice("camera").enable(timestep)

def sinosoide(ps, pe, ts, te, t):
    return ps +  (pe - ps)/2 * (1 - math.cos(math.pi*(t - ts)/(te - ts)))
# print(dir(robot.getData())
# Step 3: Any initialization you want to do for your code?
p1pan = 0
p2pan = -2*math.pi*1/8 
p3pan = 2*math.pi*1/8
p4pan = 0

p1tilt = 0 
p2tilt = -2*math.pi*1/16 
p3tilt = -2*math.pi*1/32
p4tilt = 0

pan = 0
tilt = 0

#ts = [] 
#pans = [] 
#tilts = []


# Step 4: Main continuous loop
while True:
    # Take one time step in the simulation.  At the end of this, time
    # will have advanced by (timestep).  Should the simulation run
    # into a problem (for example if you reset the simulation), this
    # will return (-1) and we should break out of the loop.
    if robot.step(timestep) == -1:
        break

    # Grab the current time.
    t = robot.getTime() 
    
    # Set the pan and tilt angles.  You will DEFINITELY want update these.
    if 0 < t and t < 2: 
        pan = sinosoide(p1pan, p2pan, 0, 2, t)
        tilt = sinosoide(p1tilt, p2tilt, 0, 2, t)
    elif 2 <= t and t < 5: 
        pan = sinosoide(p2pan, p3pan, 2, 5, t)
        tilt = sinosoide(p2tilt, p3tilt, 2, 5, t)
    elif 5 <= t and t <= 7: 
        pan = sinosoide(p3pan, p4pan, 5, 7, t)
        tilt = sinosoide(p3tilt, p4tilt, 5, 7, t)

    # Send the commands.
    tiltmotor.setPosition(tilt)
    panmotor.setPosition(pan)
    
    # Any bookkeeping you want to do?  Include the print statement to
    # graph the trajectories.
    # pans.append(pan)
    # tilts.append(tilt)
    print(t, pan, tilt) 
    
    
    # You could also break the loop at the "end of time"
    if t>=6.0:
        break


# Step 5: Clean up the code.  Nothing to do in this example.
pass
#plt.plot(ts, pans)
#plt.plot(ts, tilts)
#plt.savefig("plot1.png")
