import socket
from struct import *
import numpy as np

HOST = '10.31.48.204'    # Change this to the IP address of your Aero


def process_depth(depth):
     print "depth at [240,320]: ", depth[240,320] 
     # Fill in your code here

def get_rgb_depth_time(byte_data):
    time_stamp = unpack('q', byte_data[0:8])[0]
    rgb_size = unpack('i', byte_data[8:12])[0]
    depth_size = unpack('i', byte_data[12:16])[0] 
    rgb = np.fromstring(byte_data[16:16+rgb_size], dtype=np.uint8)
    depth = np.fromstring(byte_data[16+rgb_size:16+rgb_size+depth_size], dtype=np.uint16)
    #print depth[200*200: 200*203]
    depth = depth.reshape((480, 640))
    rgb = rgb.reshape((480,640,3))
    return rgb, depth, time_stamp



PORT = 5698              # Do not change
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    size_t_bytes = s.recv(8)
    size_t = unpack('Q', size_t_bytes)[0]
    #print "size of package: ", size_t
    byte_data = ''

    while len(byte_data) < size_t:
        byte_data += s.recv(1024 * 1024)
    s.shutdown(1)
    s.close()
    print "Received one frame"
    rgb, depth, time_stamp = get_rgb_depth_time(byte_data)
    process_average_depth(depth)

