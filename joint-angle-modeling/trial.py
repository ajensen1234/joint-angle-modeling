"""
Trial script for the project.
"""

# import the necessary packages
from trc import TRCData
import pandas as pd
import numpy as np

from functions import *
from Joint import Joint

TRIAL_PATH = 'friday/4407cd02.trc'
# For cd04, there are many missing values, so we will need to interpolate or ignore those frames.
# For cd05, RAnkle frame 93 has an empty X component.
# This is causing a NaN in the matrices it feeds into.
PROXIMAL_MATRIX_PATH = 'proximal_bone_dynamic_to_true_matrix.npy'
DISTAL_MATRIX_PATH = 'distal_bone_dynamic_to_true_matrix.npy'

# load in the actual trial data that we want to get info for
trial_data = TRCData()
trial_data.load(TRIAL_PATH)   # cd02 is walking

# General
Frames_raw = trial_data['Frame#']
Frames = pd.DataFrame(Frames_raw)

Time_raw = trial_data['Time']
Time = pd.DataFrame(Time_raw)

## Right Thigh
RASIS_raw = trial_data['RASIS']
RASIS = pd.DataFrame(RASIS_raw, columns=['X', 'Y', 'Z'])
RASIS = RASIS.to_numpy()

RPSIS_raw = trial_data['RPSIS']
RPSIS = pd.DataFrame(RPSIS_raw, columns=['X', 'Y', 'Z'])
RPSIS = RPSIS.to_numpy()

LASIS_raw = trial_data['LASIS']
LASIS = pd.DataFrame(LASIS_raw, columns=['X', 'Y', 'Z'])
LASIS = LASIS.to_numpy()

LPSIS_raw = trial_data['LPSIS']
LPSIS = pd.DataFrame(LPSIS_raw, columns=['X', 'Y', 'Z'])
LPSIS = LPSIS.to_numpy()

HipCenter = find_right_hip_center_andriacchi(RASIS=RASIS, RPSIS=RPSIS, LASIS=LASIS, LPSIS=LPSIS)

RThigh_raw = trial_data['RThigh']
RThigh = pd.DataFrame(RThigh_raw, columns=['X', 'Y', 'Z'])
RThigh = RThigh.to_numpy()

RKnee_raw = trial_data['RKnee']
RKnee = pd.DataFrame(RKnee_raw, columns=['X', 'Y', 'Z'])
RKnee = RKnee.to_numpy()

RShank_raw = trial_data['RShank']
RShank = pd.DataFrame(RShank_raw, columns=['X', 'Y', 'Z'])
RShank = RShank.to_numpy()

RAnkle_raw = trial_data['RAnkle']
RAnkle = pd.DataFrame(RAnkle_raw, columns=['X', 'Y', 'Z'])
RAnkle = RAnkle.to_numpy()

RHeel_raw = trial_data['RHeel']
RHeel = pd.DataFrame(RHeel_raw, columns=['X', 'Y', 'Z'])
RHeel = RHeel.to_numpy()

RToe_raw = trial_data['RToe']
RToe = pd.DataFrame(RToe_raw, columns=['X', 'Y', 'Z'])
RToe = RToe.to_numpy()





### Trial Phase


# Load calibration matrices
proximal_bone_dynamic_to_true_matrix = np.load(PROXIMAL_MATRIX_PATH, allow_pickle=True)
distal_bone_dynamic_to_true_matrix = np.load(DISTAL_MATRIX_PATH, allow_pickle=True)

# create proximal and dynamic reference frames
DynamicThighXAxis = RKnee - RThigh
DynamicShankXAxis = RAnkle - RShank
PBDRF_array = []
DBDRF_array = []
# TODO: make the added reference frames robust to missing data
# by including a check for NaNs in the data and leaving those frames out.
# I think this is done. Please also check the section in Joint.py at lines 29 and 36 - Sasank
for idx in range(0, len(Frames)):
    if np.isnan(RThigh[idx]).any() or np.isnan(DynamicThighXAxis[idx]).any() or np.isnan(HipCenter[idx]).any():
        print('Frame ' + str(idx) + ' has NaNs in the thigh reference frame')
        continue
    if np.isnan(RShank[idx]).any() or np.isnan(DynamicShankXAxis[idx]).any() or np.isnan(RKnee[idx]).any():
        print('Frame ' + str(idx) + ' has NaNs in the shank reference frame')
        continue
    #if not np.isnan(RThigh[idx], DynamicThighXAxis[idx], HipCenter[idx], RShank[idx], DynamicShankXAxis[idx], RKnee[idx]).any():
    if not (np.isnan(RThigh[idx]).any() or np.isnan(RShank[idx]).any() or np.isnan(DynamicThighXAxis[idx]).any() or np.isnan(DynamicShankXAxis[idx]).any() or np.isnan(HipCenter[idx]).any() or np.isnan(RKnee[idx]).any()):
        PBDRF_array = np.append(PBDRF_array, ReferenceFrame(RThigh[idx], DynamicThighXAxis[idx], HipCenter[idx], frame_index=idx))
        DBDRF_array = np.append(DBDRF_array, ReferenceFrame(RShank[idx], DynamicShankXAxis[idx], RKnee[idx], frame_index=idx))
    #print('Finished creating reference frames for frame ' + str(idx))

## Do Knee Joint Things
# create knee joint object
# PBDRF = proximal dynamic reference frame, DBDRF = distal dynamic reference frame
Knee = Joint(PBDRF_array=PBDRF_array,
            DBDRF_array=DBDRF_array,
            proximal_bone_dynamic_to_true_matrix=proximal_bone_dynamic_to_true_matrix,
            distal_bone_dynamic_to_true_matrix=distal_bone_dynamic_to_true_matrix)



print(Knee.joint_angles.shape)
print(Knee.translations.shape)

np.save('knee_joint_angles.npy', Knee.joint_angles)
np.save('knee_translations.npy',Knee.translations)












