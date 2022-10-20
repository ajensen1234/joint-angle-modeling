import numpy as np
from ReferenceFrame import ReferenceFrame


class Bone:
    def __init__(self,dynamic_reference_frame: ReferenceFrame, true_reference_frame: ReferenceFrame):
        """
        self.length, self.vectors = proximal_marker_set.vector_to_another_point(distal_marker_set)
        """
        self.dynamic = dynamic_reference_frame
        self.true = true_reference_frame
        self.dynamic_to_true_matrix = np.matmul(self.true.camera_to_local_matrix, self.dynamic.local_to_camera_matrix)
        self.camera_to_true_matrix = np.matmul(self.dynamic_to_true_matrix, self.dynamic.camera_to_local_matrix)
