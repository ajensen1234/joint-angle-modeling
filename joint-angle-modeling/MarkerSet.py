import numpy as np
import pandas as pd

class MarkerSet:
    def __init__():
    print("Please make sure to initialize your markerset using 'load_from_dataframe' or 'load_from_numpy'")
    
    def load_from_numpy(x_array,y_array,z_array):
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
