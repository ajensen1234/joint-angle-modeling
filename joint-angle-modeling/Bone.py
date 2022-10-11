import numpy as np
from MarkerSet import MarkerSet


class Bone:
    def __init__(self,proximal_marker_set, distal_marker_set):
        self.length, self.vectors = proximal_marker_set.vector_to_another_point(distal_marker_set)
        