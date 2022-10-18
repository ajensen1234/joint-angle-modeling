import numpy as np
from MarkerSet import MarkerSet


class Bone:
    def __init__(self,dynamic_marker_set: MarkerSet, true_marker_set: MarkerSet):
        """
        self.length, self.vectors = proximal_marker_set.vector_to_another_point(distal_marker_set)
        """
        self.dynamic = dynamic_marker_set
        self.true = true_marker_set
        self.dynamic_to_true_matrix = np.matmul(self.true.camera_to_local_matrix, self.dynamic.local_to_camera_matrix)
        self.camera_to_true_matrix = np.matmul(self.dynamic_to_true_matrix, self.dynamic.camera_to_local_matrix)






















