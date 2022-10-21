import numpy as np
import pandas as pd

class ReferenceFrame:
    def __init__():
        print("Please make sure to initialize your ReferenceFrame using 'load_from_dataframe' or 'load_from_numpy'")

    def __init__(self, origin: np.ndarray, x_axis: np.ndarray, z_prime_end: np.ndarray, frame_index=None):
        if frame_index is not None:
            self.frame_index = frame_index

        # these are arrays, not individual points

        # create the axes
        self.origin = origin
        self.x_axis = x_axis
        self.z_prime_end = z_prime_end
        self.z_prime = self.z_prime_end - self.origin
        self.y_axis = np.cross(self.z_prime, self.x_axis)
        self.z_axis = np.cross(self.x_axis, self.y_axis)

        # normalize the axes
        self.x_axis = np.divide(self.x_axis, np.linalg.norm(self.x_axis))
        self.y_axis = np.divide(self.y_axis, np.linalg.norm(self.y_axis))
        self.z_axis = np.divide(self.z_axis, np.linalg.norm(self.z_axis))

        """
        # average axes to get the final axes
        self.x_axis = np.average(self.x_axis, axis=0)
        self.y_axis = np.average(self.y_axis, axis=0)
        self.z_axis = np.average(self.z_axis, axis=0)
        """


        # arrays of x,y,z coordinates
        self.x_ = None
        self.y_ = None
        self.z_ = None

        self.local_to_camera_matrix = self.create_transformation_matrix(x_axis=self.x_axis, y_axis=self.y_axis, z_axis=self.z_axis, origin=self.origin)
        self.camera_to_local_matrix = np.linalg.inv(self.local_to_camera_matrix)

    def create_transformation_matrix(self, x_axis, y_axis, z_axis, origin):
        temp = np.array([x_axis, y_axis, z_axis])

        # assert that the rotation matrices are good

        np.testing.assert_almost_equal(np.transpose(temp), np.linalg.inv(temp), decimal=3,
                                err_msg='The rotation matrix is not orthogonal')
        np.testing.assert_almost_equal(np.linalg.det(temp), 1 or -1, decimal=3,
                                err_msg="Rotation matrix determinant is not zero!")

        temp = np.append(temp, [origin], axis=0)
        temp = np.append(temp, np.array([[0],[0],[0],[1]]), axis=1).T
        #print(temp)
        return temp
    
    def normalize_axis(self, axis) -> np.ndarray:
        axis = axis / sum(list(axis))
        return axis

    def load_from_numpy(self, x_array,y_array,z_array):
        self.x_ = x_array
        self.y_ = y_array
        self.z_ = z_array
    
    def load_from_dataframe(self,df,number):
        self.grab_point(df,number)

    def grab_point(self,df,point):
        x = "X" + str(point)
        y = "Y" + str(point)
        z = "Z" + str(point)
        self.x_ = np.array(df[x])
        self.y_ = np.array(df[y])
        self.z_ = np.array(df[z])
    
    def vector_to_another_point(self,marker_set):
        return self.create_vector(self,marker_set)
    
    def vector_from_another_point(self,marker_set):
        return self.create_vector(marker_set,self)
        
    def create_vector(self,start_point, end_point):
        x_diff = end_point.x_ - start_point.x_
        y_diff = end_point.y_ - start_point.y_
        z_diff = end_point.z_ - start_point.z_
        
        norm = np.linalg.norm(np.array([x_diff, y_diff, z_diff]).T,axis = 1)
        x_dir = np.divide(x_diff,norm)
        y_dir = np.divide(y_diff,norm)
        z_dir = np.divide(z_diff,norm)
        return norm, np.array([x_dir, y_dir, z_dir]).T
