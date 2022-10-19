import numpy as np
from Bone import Bone
from MarkerSet import MarkerSet

class Joint:
    def __init__(self, PBDMS: list, DBDMS: list, proximal_bone_dynamic_to_true_matrix, distal_bone_dynamic_to_true_matrix):
        self.PBDMS = PBDMS
        self.DBDMS = DBDMS
        self.proximal_bone_dynamic_to_true_matrix = proximal_bone_dynamic_to_true_matrix
        self.distal_bone_dynamic_to_true_matrix = distal_bone_dynamic_to_true_matrix
        self.joint_angles, self.translations = self.calculate_joint_geometry()
        
    def calculate_joint_geometry(self) -> list, list:
        proximal_camera_to_true_matrices= []
        distal_camera_to_true_matrices = []
        joint_transformation_matrices = []
        joint_angles = []
        translations = []
        for idx, frame in enumerate(Frames):
            proximal_camera_to_true_matrices.append(np.matmul(self.proximal_bone_dynamic_to_true_matrix, self.PBDMS[idx].camera_to_local_matrix))
            distal_camera_to_true_matrices.append(np.matmul(self.distal_bone_dynamic_to_true_matrix, self.DBDMS[idx].camera_to_local_matrix))
            # the below line should not go out of bounds because the proximal and distal bone matrix elements it needs have just been created
            joint_transformation_matrices.append(np.matmul(proximal_camera_to_true_matrices[idx], np.linalg.inv(distal_camera_to_true_matrices[idx])))
            
            # calculate joint angles
            # TODO: check this and account for angles that fall outside of the range of the arccos and arcsin functions
            x_angle = (np.arcsin(joint_transformation_matrices[idx][2][1]))
            y_angle = (np.arccos(joint_transformation_matrices[idx][2][2]/np.cos(x_angle)))
            z_angle = (np.arccos(joint_transformation_matrices[idx][1][1]/np.cos(x_angle)))
            joint_angles.append([x_angle, y_angle, z_angle])

            # calculate joint translations
            # TODO: check this lol
            x_translation = joint_transformation_matrices[idx][0][3]
            y_translation = joint_transformation_matrices[idx][1][3]
            z_translation = joint_transformation_matrices[idx][2][3]
            translations.append([x_translation, y_translation, z_translation])


        return joint_angles, translations













        """
        self.Joint_Angles = np.empty(self.proximal_bone.length.shape[0])
        for idx in range(self.proximal_bone.length.shape[0]):
            prox_vec = self.proximal_bone.vectors[idx]
            dist_vec = self.distal_bone.vectors[idx]
            
            self.Joint_Angles[idx] = np.rad2deg(np.arccos(np.dot(dist_vec,prox_vec)))       
        """
