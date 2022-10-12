from MarkerSet import *
import numpy as np

def find_right_hip_center_andriacchi(RASIS, RPSIS, LASIS, LPSIS):
    psis_midpoint_x = 0.5*(RPSIS.x_ + LPSIS.x_)
    psis_midpoint_y = 0.5*(RPSIS.y_ + LPSIS.y_)
    psis_midpoint_z = 0.5*(RPSIS.z_ + LPSIS.z_)

    
    HC_x = 0.5*(RASIS.x_ + psis_midpoint_x)
    HC_y = 0.5*(RASIS.y_ + psis_midpoint_y)
    HC_z = 0.5*(RASIS.z_ + psis_midpoint_z) 
