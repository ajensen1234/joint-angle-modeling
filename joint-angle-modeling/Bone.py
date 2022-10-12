import numpy as np
from MarkerSet import MarkerSet


class Bone:
    def __init__(self,proximal_marker_set, distal_marker_set):
        self.length, self.vectors = proximal_marker_set.vector_to_another_point(distal_marker_set)

    def define_x_axis(self, starting_marker_set, ending_marker_set):
        self.x_mag, self.x_vec = ending_marker_set.vector_from_another_point(starting_marker_set)
        
    def define_y_axis(self, z_prime_marker):
        ## Cross product between x and z_prime

    def define_z_axis(self):
        
