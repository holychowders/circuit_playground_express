"""
This function endeavors to help users locate bugs by calling it throughout
their CPX code, invoking user-definable feedback from the onboard NeoPixels,
dependent upon immediate call paths or positions.

Author: https://github.com/holychowders
"""

from adafruit_circuitplayground.express import cpx
from time import sleep


def vis_db(ind=0, col='green', on_t=0.2, off_t=0.5):
    """
    Flash a NeoPixel of given color; flash green if no arguments.
    ind takes NeoPixel index; default 0.
    col takes RGB tuple or str of color name; default 'green'.
    on/off sets duration (seconds) for color on/off; default .5 and .2.
    """
    
    colors_dict = {
        col: col, 'red':(20,0,0), 'green':(0,20,0), 'blue':(0,0,20),
        'orange':(20,8,0), 'yellow':(20,18,0), 'purple':(20,0,10)
    }

    cpx.pixels[ind] = colors_dict[col]
    sleep(on_t)

    cpx.pixels[ind] = (0, 0, 0)
    sleep(off_t)
