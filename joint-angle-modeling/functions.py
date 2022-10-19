from MarkerSet import *
import numpy as np

def MidPoint(marker1: tuple, marker2: tuple) -> tuple:
    # This function finds the midpoint between two markers for each frame in the data
    # Thus, the inputs and outputs are tuples of tuples.

    MidPoint_tuple = ()
    for idx, (i, j) in enumerate(zip(marker1, marker2)):
        MidPoint_tuple += (i[0] + (j[0]-i[0])/2, i[1] + (j[1]-i[1])/2, i[2] + (j[2]-i[2])/2),
    return MidPoint_tuple

def find_right_hip_center_andriacchi(RASIS: tuple, RPSIS: tuple, LASIS: tuple, LPSIS: tuple) -> tuple:

    """
    This function finds the right hip center using the Andriacchi method.

    Pseudocode:
    RightHipCenter = MidPoint(RASIS, MidPoint(RPSIS, LPSIS)) - 15z
    """

    RightHipCenter = MidPoint(RASIS, MidPoint(RPSIS, LPSIS))
    for idx, i in enumerate(RightHipCenter):
        RightHipCenter[idx] = i[0], i[1], i[2] - 15

    return RightHipCenter
