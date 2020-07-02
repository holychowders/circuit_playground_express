from adafruit_circuitplayground.express import cpx
from time import sleep

RAINBOW_RGBS_10 = (
    (15, 0, 0), (15, 5, 0), (15, 15, 0), (0, 15, 0), (2, 8, 2),
    (0, 15, 15), (0, 0, 15), (0, 0, 6), (15, 0, 15), (4, 0, 8)
)

def run_rainbow_iter(speed=4, pause=0.0):
    """
    Iterate individual NeoPixels through rainbow and iterate back to black.
    Optional speed argument takes int between 1 and 10; default 4
    pause takes float for seconds between each iteration in/out; default 
    """
    if type(speed) != int:
        raise TypeError("speed takes int between 1 and 10")
    if not (1 <= speed <= 10):
        raise ValueError("speed must be between 1 and 10")
    if type(pause) != float and type(pause) != int:
        raise TypeError("pause takes non-negative float")
    if not (pause >= 0):
        raise ValueError("pause takes non-negative float")


    speed = .3/speed

    for pixel, color in enumerate(RAINBOW_RGBS_10):
        sleep(speed)
        cpx.pixels[pixel] = color

    sleep(pause)

    for pixel in range(10):
        sleep(speed)
        cpx.pixels[pixel] = (0,0,0)

    sleep(pause)
