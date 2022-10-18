import numpy as np
from Bone import Bone
from MarkerSet import MarkerSet

class Joint:
    def __init__(self,proximal_bone_dynamic_marker_set: MarkerSet, distal_bone_dynamic_marker_set: MarkerSet, proximal_bone_dynamic_to_true_matrix, distal_bone_dynamic_to_true_matrix):
        self.proximal_bone_dynamic_marker_set = proximal_bone_dynamic_marker_set
        self.distal_bone_dynamic_marker_set = distal_bone_dynamic_marker_set
        self.joint_angles = self.calculate_joint_angle()
        
    def calculate_joint_angle(self):
        self.Joint_Angles = np.empty(self.proximal_bone.length.shape[0])
        for idx in range(self.proximal_bone.length.shape[0]):
            prox_vec = self.proximal_bone.vectors[idx]
            dist_vec = self.distal_bone.vectors[idx]
            
            self.Joint_Angles[idx] = np.rad2deg(np.arccos(np.dot(dist_vec,prox_vec)))       
