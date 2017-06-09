# Intel-Aero-data-client

# Run this program on Aero
## Connect Aero

Connect Aero to your computer using USB cable

## ssh into Aero

If you are using Windows, open a putty and connect to 192.168.7.2

If you are using Ubuntu or Mac, open a terminal

```
ssh root@169.168.7.2
```

## run docker container that has this program pre-built

```
docker run -it --privileged -p 5698:5698 ros_rs_dc
```

## run this program inside aero to stream RGB-D data

```
cd ~/Intel-Aero-data-client/build
./DataClinet
```

# Copy and run the program to receive RGB-D data on your computer
(Install python on your computer if you do not know what it is by following this link)  
 Windowns x64 https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh  
 Windowns x32 https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86.sh  
 Mac https://repo.continuum.io/archive/Anaconda2-4.4.0-MacOSX-x86_64.pkg  


Then open another terminal or putty

```
git clone https://github.com/UCM-ME190/Intel-Aero-data-client.git
cd Intel-Aero-data-client/python
python receiver.py
```
After getting this output, you have all the tools. Now let us develop a simple collision detection program

## Make your own collision detection program

Find Intel-Aero-data-client/python folder on your computer and open receiver.py using a text editor

``` Python
def process_depth(depth):
     print "depth at [240,320]: ", depth[240,320] 
     # Fill in your code here
```

After line 9 is where your code should go. 

### Convert depth from millimeters to meters.
parameter depth is a 2D numpy array of shape (480,640).

### Calcuate average depth

Because each pixel in depth map has its depth value. To make it simple, we use average of depth as a distance of Aero to an obstacle. Write code to calculate depth mean in meters 

### Print different message based on average depth value

Use the average depth you just get to print out “safe” if it is larger than 2 meter, and “obstacle” when average depth is less than 2 meter.

