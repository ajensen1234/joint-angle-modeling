import numpy as np
import pandas as pd
from trc import TRCData

#data = pd.read_csv('friday/4407cd01.trc')
mocap_data = TRCData()
mocap_data.load('friday/4407cd01.trc')
#print(mocap_data)
#RThigh = mocap_data['RThigh']
#print(RThigh)


RKnee = mocap_data['RKnee']
RKnee_frame = pd.DataFrame(RKnee, columns=['X', 'Y', 'Z'])

print(RKnee_frame)

RMedKnee = mocap_data['RMed.Knee']
RMedKnee_frame = pd.DataFrame(RMedKnee, columns=['X', 'Y', 'Z'])

pls_work = RKnee_frame-RMedKnee_frame
pls_work = tuple(pls_work.itertuples(index=False, name=None))

RThigh = mocap_data['RThigh']
RThigh_frame = pd.DataFrame(RThigh, columns=['X', 'Y', 'Z'])
RThigh_frame = tuple(RThigh_frame.itertuples(index=False, name=None))
crossyboy = np.cross(pls_work, RThigh_frame)
print(type(crossyboy))

#crossyboy = crossyboy / np.linalg.norm(crossyboy, axis=1)[:,:]
for idx, point in enumerate(crossyboy):
    #crossyboy[point] = point / np.linalg.norm(point) 
    crossyboy[idx] = point / sum(list(point))


print(type(crossyboy))
crossyboy = np.average(crossyboy, axis=0)
print(crossyboy.size)
#print(crossyboy)
temp = np.array([[1,1,1],[2,2,2],[3,3,3],[4,4,4]])
#print(temp)
temp = np.append(temp, np.array([[0],[0],[0],[1]]), axis=1).T
print(temp)

# good_thing = dynamic_to_femur x Thigh.camera_to_local_matrix x camera_data

#print(pls_work)