from time import sleep
from adafruit_circuitplayground.express import cpx


def run_rainbow_fade(speed=5, brightness=2, pause=0.0):
    """
    Iteratively fade the NeoPixels through the colors of the rainbow.
    pause is hold duration (seconds) between colors; default 0.0. 
    """
    if type(speed) != type(brightness) != int:
        raise TypeError("speed and brightness take int values")
    if not (1 <= speed <= 10):
        raise ValueError("speed takes int between 1 and 10")
    if not (1 <= brightness <= 10):
        raise ValueError("brightness takes int between 0 and 10")

    RAINBOW_RGBS_6 = (
        (15, 0, 0), (20, 3, 0), (15, 8, 0), (0, 15, 0), (0, 8, 15), (15, 0, 10)
    )

    # brightness factor
    bf = brightness
    speed = .7/speed
    color = 0

    while color < 6:
        r, g, b = RAINBOW_RGBS_6[color % 6]

        for pixel in range(10):
            sleep(speed)
            cpx.pixels[pixel] = (bf*r, bf*g, bf*b)

        sleep(pause)
        color += 1
