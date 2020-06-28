"""
Author: https://github.com/holychowders
"""

from adafruit_circuitplayground.express import cpx
from time import sleep


def bi_pride_flag(aspect='horizontal', glow=False, glow_pause=10):
    """
    Map bisexual pride flag to NeoPixels in horizontal/vertical configuration
    with optional momentary glow. All arguments optional.
    aspect takes 'horizontal' or 'vertical'; default 'horizontal'.
    glow takes bool; default False.
    glow_pause sets duration (seconds) of pause between momentary glow; default 10.
    """
    GLOW_FADE_T = 0.025

    def map_pixels(bf=5):
        """
        Map NeoPixels according to aspect.
        Takes optional bf (brightness factor) to allow fading in run_with_glow; default 5.
        """

        if aspect == 'horizontal':
            cpx.pixels[0] = cpx.pixels[1] = cpx.pixels[9] = cpx.pixels[8] = (bf*5, 0, bf*2)
            cpx.pixels[2] = cpx.pixels[7] = (20, 0, 40)
            cpx.pixels[3] = cpx.pixels[4] = cpx.pixels[6] = cpx.pixels[5] = (0, 0, bf*5)
        elif aspect == 'vertical':
            cpx.pixels[0] = cpx.pixels[9] = cpx.pixels[4] = cpx.pixels[5] = (bf*5, 0, bf*10)
            cpx.pixels[1] = cpx.pixels[2] = cpx.pixels[3] = (bf*5, 0, bf*2)
            cpx.pixels[8] = cpx.pixels[7] = cpx.pixels[6] = (0, 0, bf*5)

    def run_with_glow():
        for bf in range(3, 15):
            sleep(GLOW_FADE_T)
            map_pixels(bf)

        sleep(.2)

        for bf in range(14, 2, -1):
            sleep(GLOW_FADE_T)
            map_pixels(bf)

        sleep(glow_pause)


    if glow == True:
        run_with_glow()

    elif glow == False:
        map_pixels()
        
