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
#print(type(RThigh_frame))
print(pls_work)
print(RThigh_frame)
for row in RThigh_frame:
    print(row)
#print(list(RThigh_frame))
#asdf = pls_work - RThigh_frame
#asdf_tuple = tuple(ti / 2 for ti in asdf)
#lambda_test = tuple(map(lambda i, j: i - j, pls_work, RThigh_frame))
#print(lambda_test)
new_tuple = ()
for idx, (i, j) in enumerate(zip(pls_work, RThigh_frame)):
    new_tuple += (i[0] - j[0], i[1] - j[1], i[2] - j[2]),

print(new_tuple)

# midpoint(m1,m2) = m1 + ((m2 - m1) / 2)

#crossyboy = crossyboy / np.linalg.norm(crossyboy, axis=1)[:,:]
for idx, point in enumerate(crossyboy):
    #crossyboy[point] = point / np.linalg.norm(point) 
    crossyboy[idx] = point / sum(list(point))


#print(type(crossyboy))
crossyboy = np.average(crossyboy, axis=0)
#print(crossyboy.size)
#print(crossyboy)
temp = np.array([[1,1,1],[2,2,2],[3,3,3],[4,4,4]])
#print(temp)
temp = np.append(temp, np.array([[0],[0],[0],[1]]), axis=1).T
#print(temp)

# good_thing = dynamic_to_femur x Thigh.camera_to_local_matrix x camera_data

#print(pls_work)