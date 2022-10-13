import numpy as np 
import matplotlib.pyplot as plt 

pan = 0 
tilt = 0 

def sinosoide(ps, pe, ts, te, t):
    '''Helper function that returns the calculation of the sinosoide that we went through in class'''
    return ps +  (pe - ps)/2 * (1 - np.cos(np.pi*(t - ts)/(te - ts)))
  
def plot1():
    '''The control sequence for the second assignment'''
    pans = [] 
    tilts = [] 
    # Array simulating time 
    ts = np.array(range(1, 401))*0.01
    
    # Initial values 
    start_state_pan = 0
    start_state_tilt = 0
    end_state_pan = 2*np.pi*7/8 - 2*np.pi
    end_state_tilt = 2*np.pi*15/16 - 2*np.pi
     

    for t in ts:
        # Control sequence 
        if 0 < t and t < 1: 
            pan = 0
            tilt = 0
        elif 1 < t and t < 3: 
            pan = sinosoide(start_state_pan, end_state_pan, 1, 3, t)
            tilt = sinosoide(start_state_tilt, end_state_tilt, 1, 3, t)
        elif 3 < t: 
            pan = end_state_pan
            tilt = end_state_tilt 

        pans.append(pan)
        tilts.append(tilt)
        print(t, pan, tilt) 


    pans = np.array(pans)
    tilts = np.array(tilts)

    print(len(pans), len(tilts), )
    plt.plot(ts, pans)
    plt.plot(ts, tilts)
    plt.plot(np.array([0, 1, 3]), np.array([0, 0, end_state_pan]), "o")
    plt.plot(np.array([0, 1, 3]), np.array([0, 0, end_state_tilt]), "o")
    plt.title("Problem 2")
    plt.savefig("plot1.png")
    plt.clf()
    
def plot2():
    # Initialization for the 3rd problem 
    pans = [] 
    tilts = [] 
    ts = np.array(range(1, 701))*0.01
    
    p1pan = 0
    p2pan = -2*np.pi*1/8 
    p3pan = 2*np.pi*1/8
    p4pan = 0
    
    p1tilt = 0 
    p2tilt = -2*np.pi*1/16 
    p3tilt = -2*np.pi*1/32
    p4tilt = 0

    # Controls 
    for t in ts:
        if 0 < t and t < 2: 
            pan = sinosoide(p1pan, p2pan, 0, 2, t)
            tilt = sinosoide(p1tilt, p2tilt, 0, 2, t)
        elif 2 <= t and t < 5: 
            pan = sinosoide(p2pan, p3pan, 2, 5, t)
            tilt = sinosoide(p2tilt, p3tilt, 2, 5, t)
        elif 5 <= t and t <= 7: 
            pan = sinosoide(p3pan, p4pan, 5, 7, t)
            tilt = sinosoide(p3tilt, p4tilt, 5, 7, t)

        pans.append(pan)
        tilts.append(tilt)
        print(t, pan, tilt) 


    pans = np.array(pans)
    tilts = np.array(tilts)

    print(len(pans), len(tilts), )
    plt.plot(ts, pans)
    plt.plot(ts, tilts)
    plt.plot(np.array([0, 2, 5, 7]), np.array([p1pan, p2pan, p3pan, p4pan]), "o")
    plt.plot(np.array([0, 2, 5, 7]), np.array([p1tilt, p2tilt, p3tilt, p4tilt]), "o")
    plt.title("Problem 3")
    plt.savefig("plot2.png")
    plt.clf()

def plot3():
    # Initialization for problem 4 
    pans = [] 
    tilts = [] 
    ts = np.array(range(1, 701))*0.01
    
    p1pan = 0
    v1pan = 0 
    p2pan = -2*np.pi*1/8
    v2pan = 0  
    p3pan = 2*np.pi*1/8
    v3pan = 0
    p4pan = 0
    v4pan = 0
    
    p1tilt = 0 
    v1tilt = 0
    p2tilt = -2*np.pi*1/16
    v2tilt = 0 
    p3tilt = -2*np.pi*1/32
    v3tilt = 0
    p4tilt = 0
    v4tilt = 0
    
    t1 = 0
    t2 = 2
    t3 = 5
    t4 = 7
    
    # Calculate matrices and iverse 
    t1p = np.array([1, t1, t1**2, t1**3]) 
    t1v = np.array([0, 1, 2*t1, 3*t1**2])
    t2p = np.array([1, t2, t2**2, t2**3]) 
    t2v = np.array([0, 1, 2*t2, 3*t2**2]) 
    t3p = np.array([1, t3, t3**2, t3**3]) 
    t3v = np.array([0, 1, 2*t3, 3*t3**2]) 
    t4p = np.array([1, t4, t4**2, t4**3]) 
    t4v = np.array([0, 1, 2*t4, 3*t4**2]) 
     
    m12 = np.array([t1p, t1v, t2p, t2v])
    m23 = np.array([t2p, t2v, t3p, t3v])
    m34 = np.array([t3p, t3v, t4p, t4v])
    
    minv12 = np.linalg.inv(m12) 
    minv23 = np.linalg.inv(m23) 
    minv34 = np.linalg.inv(m34) 
    
    ct12pan = minv12 @ np.array([p1pan, v1pan, p2pan, v2pan])
    ct23pan = minv23 @ np.array([p2pan, v2pan, p3pan, v3pan])
    ct34pan = minv34 @ np.array([p3pan, v3pan, p4pan, v4pan])
    ct12tilt = minv12 @ np.array([p1tilt, v1tilt, p2tilt, v2tilt])
    ct23tilt = minv23 @ np.array([p2tilt, v2tilt, p3tilt, v3tilt])
    ct34tilt = minv34 @ np.array([p3tilt, v3tilt, p4tilt, v4tilt])

    # Do control sequence 
    for t in ts:
        vt = np.array([1, t, t**2, t**3])
        
        if 0 < t and t < 2: 
            pan = ct12pan @ vt
            tilt = ct12tilt @ vt
        elif 2 <= t and t < 5: 
            pan = ct23pan @ vt
            tilt = ct23tilt @ vt
        elif 5 <= t and t < 7: 
            pan = ct34pan @ vt
            tilt = ct34tilt @ vt
            

        pans.append(pan)
        tilts.append(tilt)
        # print(t, pan, tilt) 


    pans = np.array(pans)
    tilts = np.array(tilts)

    plt.plot(ts, pans)
    plt.plot(ts, tilts)
    plt.plot(np.array([t1, t2, t3, t4]), np.array([p1pan, p2pan, p3pan, p4pan]), "o")
    plt.plot(np.array([t1, t2, t3, t4]), np.array([p1tilt, p2tilt, p3tilt, p4tilt]), "o")
    plt.title("Problem 4")
    plt.savefig("plot3.png")
    plt.clf()

def plot4():
    # Initialization for problem 5
    pans = [] 
    tilts = [] 
    ts = np.array(range(1, 701))*0.01
    
    p1pan = 0
    v1pan = 0 
    p2pan = -2*np.pi*1/8
    v2pan = 0  
    p3pan = 2*np.pi*1/8
    v3pan = np.pi/2
    p4pan = 0
    v4pan = 0
    
    p1tilt = 0 
    v1tilt = 0
    p2tilt = -2*np.pi*1/16
    v2tilt = np.pi/2
    p3tilt = -2*np.pi*1/32
    v3tilt = 0
    p4tilt = 0
    v4tilt = 0
    
    t1 = 0
    t2 = 2
    t3 = 5
    t4 = 7
    
    # Calculate control sequence 
    t1p = np.array([1, t1, t1**2, t1**3]) 
    t1v = np.array([0, 1, 2*t1, 3*t1**2])
    t2p = np.array([1, t2, t2**2, t2**3]) 
    t2v = np.array([0, 1, 2*t2, 3*t2**2]) 
    t3p = np.array([1, t3, t3**2, t3**3]) 
    t3v = np.array([0, 1, 2*t3, 3*t3**2]) 
    t4p = np.array([1, t4, t4**2, t4**3]) 
    t4v = np.array([0, 1, 2*t4, 3*t4**2]) 
     
    m12 = np.array([t1p, t1v, t2p, t2v])
    m23 = np.array([t2p, t2v, t3p, t3v])
    m34 = np.array([t3p, t3v, t4p, t4v])
    
    minv12 = np.linalg.inv(m12) 
    minv23 = np.linalg.inv(m23) 
    minv34 = np.linalg.inv(m34) 
    
    ct12pan = minv12 @ np.array([p1pan, v1pan, p2pan, v2pan])
    ct23pan = minv23 @ np.array([p2pan, v2pan, p3pan, v3pan])
    ct34pan = minv34 @ np.array([p3pan, v3pan, p4pan, v4pan])
    ct12tilt = minv12 @ np.array([p1tilt, v1tilt, p2tilt, v2tilt])
    ct23tilt = minv23 @ np.array([p2tilt, v2tilt, p3tilt, v3tilt])
    ct34tilt = minv34 @ np.array([p3tilt, v3tilt, p4tilt, v4tilt])

    # Do control 
    for t in ts:
        vt = np.array([1, t, t**2, t**3])
        
        if 0 < t and t < 2: 
            pan = ct12pan @ vt
            tilt = ct12tilt @ vt
        elif 2 <= t and t < 5: 
            pan = ct23pan @ vt
            tilt = ct23tilt @ vt
        elif 5 <= t and t < 7: 
            pan = ct34pan @ vt
            tilt = ct34tilt @ vt
            

        pans.append(pan)
        tilts.append(tilt)
        # print(t, pan, tilt) 


    pans = np.array(pans)
    tilts = np.array(tilts)

    plt.plot(ts, pans)
    plt.plot(ts, tilts)
    plt.plot(np.array([t1, t2, t3, t4]), np.array([p1pan, p2pan, p3pan, p4pan]), "o")
    plt.plot(np.array([t1, t2, t3, t4]), np.array([p1tilt, p2tilt, p3tilt, p4tilt]), "o")
    plt.title("Problem 5")
    plt.savefig("plot4.png")
    plt.clf()

def plot5():
    # Problem 6
    pans = [] 
    tilts = [] 
    ts = np.array(range(1, 701))*0.01
    
    # Define the first path
    p1pan = -2*np.pi
    v1pan = 0 
    p2pan = 0
    v2pan = np.pi/2
    
    p1tilt = -2*np.pi
    v1tilt = 0
    p2tilt = 0
    v2tilt = np.pi/8
    
    t1 = 0
    t2 = 1
    t3 = 7
    
    # Calculate control law
    t1p = np.array([1, t1, t1**2, t1**3]) 
    t1v = np.array([0, 1, 2*t1, 3*t1**2])
    t2p = np.array([1, t2, t2**2, t2**3]) 
    t2v = np.array([0, 1, 2*t2, 3*t2**2]) 
     
    m12 = np.array([t1p, t1v, t2p, t2v])
    
    minv12 = np.linalg.inv(m12) 
    
    ct12pan = minv12 @ np.array([p1pan, v1pan, p2pan, v2pan])
    ct12tilt = minv12 @ np.array([p1tilt, v1tilt, p2tilt, v2tilt])
    
    # Use control sequence 
    for t in ts:
        vt = np.array([1, t, t**2, t**3])
        
        if 0 < t and t < 1: 
            pan = ct12pan @ vt
            tilt = ct12tilt @ vt
        elif 1 <= t: 
            pan = np.pi/2 * np.sin(t - t2) 
            tilt = np.pi/4 * np.sin((t - t2)/2) 

        pans.append(pan)
        tilts.append(tilt)
        # print(t, pan, tilt) 


    pans = np.array(pans)
    tilts = np.array(tilts)

    plt.plot(ts, pans)
    plt.plot(ts, tilts)
    plt.plot(np.array([t1, t2]), np.array([p1pan, p2pan]), "o")
    plt.plot(np.array([t1, t2]), np.array([p1tilt, p2tilt]), "o")
    plt.title("Problem 6")
    plt.savefig("plot5.png")
    plt.clf()

plot1()
plot2()
plot3()
plot4()
plot5()

