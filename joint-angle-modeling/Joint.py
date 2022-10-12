import numpy as np
from Bone import Bone
from MarkerSet import MarkerSet

class Joint:
    def __init__(self,proximal_bone,distal_bone):
        self.proximal_bone = proximal_bone
        self.distal_bone = distal_bone
        self.calculate_joint_angle()
        
    def calculate_joint_angle(self):
        self.Joint_Angles = np.empty(self.proximal_bone.length.shape[0])
        for idx in range(self.proximal_bone.length.shape[0]):
            prox_vec = self.proximal_bone.vectors[idx]
            dist_vec = self.distal_bone.vectors[idx]
            
            self.Joint_Angles[idx] = np.rad2deg(np.arccos(np.dot(dist_vec,prox_vec)))       
