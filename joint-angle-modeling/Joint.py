import numpy as np
from Bone import Bone
from ReferenceFrame import ReferenceFrame

class Joint:
    def __init__(self, PBDRF_array: np.array, DBDRF_array: np.array, proximal_bone_dynamic_to_true_matrix, distal_bone_dynamic_to_true_matrix):
        self.PBDRF_array = PBDRF_array
        self.DBDRF_array = DBDRF_array
        self.proximal_bone_dynamic_to_true_matrix = proximal_bone_dynamic_to_true_matrix
        self.distal_bone_dynamic_to_true_matrix = distal_bone_dynamic_to_true_matrix
        self.joint_angles, self.translations = self.calculate_joint_geometry()
        
    def calculate_joint_geometry(self):
        joint_angles = []
        translations = []
        for idx, (i,j) in enumerate(zip(self.PBDRF_array, self.DBDRF_array)):

            proximal_camera_to_true_matrix = np.matmul(self.proximal_bone_dynamic_to_true_matrix, self.PBDRF_array[idx].camera_to_local_matrix)
            distal_camera_to_true_matrix = np.matmul(self.distal_bone_dynamic_to_true_matrix, self.DBDRF_array[idx].camera_to_local_matrix)
            joint_transformation_matrix = np.matmul(proximal_camera_to_true_matrix, np.linalg.inv(distal_camera_to_true_matrix))
            #print(joint_transformation_matrix)
            
            # calculate joint angles
            # TODO: check this and account for angles that fall outside of the range of the arccos and arcsin functions
            x_angle = (np.arcsin(joint_transformation_matrix[2][1]))
            y_angle = (np.arccos(joint_transformation_matrix[2][2]/np.cos(x_angle)))
            z_angle = (np.arccos(joint_transformation_matrix[1][1]/np.cos(x_angle)))
            joint_angles = np.append(joint_angles, [x_angle, y_angle, z_angle])

            # calculate joint translations
            # TODO: check this lol
            x_translation = joint_transformation_matrix[0][3]
            y_translation = joint_transformation_matrix[1][3]
            z_translation = joint_transformation_matrix[2][3]
            translations = np.append(translations, [x_translation, y_translation, z_translation])


        return joint_angles, translations













        """
        self.Joint_Angles = np.empty(self.proximal_bone.length.shape[0])
        for idx in range(self.proximal_bone.length.shape[0]):
            prox_vec = self.proximal_bone.vectors[idx]
            dist_vec = self.distal_bone.vectors[idx]
            
            self.Joint_Angles[idx] = np.rad2deg(np.arccos(np.dot(dist_vec,prox_vec)))       
        """
