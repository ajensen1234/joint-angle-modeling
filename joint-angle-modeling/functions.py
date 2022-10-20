from ReferenceFrame import *
import numpy as np

def MidPoint(marker1: np.ndarray, marker2: np.ndarray) -> np.ndarray:
    # This function finds the midpoint between two markers for each frame in the data
    # Thus, the inputs and outputs are tuples of tuples.

    MidPoint_array = marker1 + ((marker2 - marker1) / 2)
    """
    for idx, (i, j) in enumerate(zip(marker1, marker2)):
        MidPoint_array += (i[0] + (j[0]-i[0])/2, i[1] + (j[1]-i[1])/2, i[2] + (j[2]-i[2])/2),
    """
    return MidPoint_array

def find_right_hip_center_andriacchi(RASIS: np.ndarray, RPSIS: np.ndarray, LASIS: np.ndarray, LPSIS: np.ndarray) -> np.ndarray:

    """
    This function finds the right hip center using the Andriacchi method.

    Pseudocode:
    RightHipCenter = MidPoint(RASIS, MidPoint(RPSIS, LPSIS)) - 15z
    """

    RightHipCenter = MidPoint(RASIS, MidPoint(RPSIS, LPSIS))
    for idx, i in enumerate(RightHipCenter):
        RightHipCenter[idx] = i[0], i[1], i[2] - 15

    return RightHipCenter
