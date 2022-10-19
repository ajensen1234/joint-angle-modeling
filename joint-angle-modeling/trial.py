"""
Trial script for the project.
"""

# import the necessary packages
from trc import TRCData
import pandas as pd
import numpy as np

from functions import *

TRIAL_PATH = '../friday/4407cd02.trc'
PROXIMAL_MATRIX_PATH = ''
DISTAL_MATRIX_PATH = ''


# General
Frames_raw = calib_data['Frames']
Frames = pd.DataFrame(Frames_raw)

Time_raw = calib_data['Time']
Time = pd.DataFrame(Time_raw)

## Right Thigh
RASIS_raw = calib_data['RASIS']
RASIS = pd.DataFrame(RASIS_raw, columns=['X', 'Y', 'Z'])
RASIS = tuple(RASIS.itertuples(index=False, name=None))

RPSIS_raw = calib_data['RPSIS']
RPSIS = pd.DataFrame(RPSIS_raw, columns=['X', 'Y', 'Z'])
RPSIS = tuple(RPSIS.itertuples(index=False, name=None))

LASIS_raw = calib_data['LASIS']
LASIS = pd.DataFrame(LASIS_raw, columns=['X', 'Y', 'Z'])
LASIS = tuple(LASIS.itertuples(index=False, name=None))

RThigh_raw = calib_data['RThigh']
RThigh = pd.DataFrame(RThigh_raw, columns=['X', 'Y', 'Z'])
RThigh = tuple(RThigh.itertuples(index=False, name=None))

RKnee_raw = calib_data['RKnee']
RKnee = pd.DataFrame(RKnee_raw, columns=['X', 'Y', 'Z'])
RKnee = tuple(RKnee.itertuples(index=False, name=None))

RMedKnee_raw = calib_data['RMed.Knee']
RMedKnee = pd.DataFrame(RMedKnee_raw, columns=['X', 'Y', 'Z'])
RMedKnee = tuple(RMedKnee.itertuples(index=False, name=None))

# Right Shank
#RKnee
#RMedKnee
RShank_raw = calib_data['RShank']
RShank = pd.DataFrame(RShank_raw, columns=['X', 'Y', 'Z'])
RShank = tuple(RShank.itertuples(index=False, name=None))

RAnkle_raw = calib_data['RAnkle']
RAnkle = pd.DataFrame(RAnkle_raw, columns=['X', 'Y', 'Z'])
RAnkle = tuple(RAnkle.itertuples(index=False, name=None))

RMedAnkle_raw = calib_data['RMed.Ankle']
RMedAnkle = pd.DataFrame(RMedAnkle_raw, columns=['X', 'Y', 'Z'])
RMedAnkle = tuple(RMedAnkle.itertuples(index=False, name=None))

RHeel_raw = calib_data['RHeel']
RHeel = pd.DataFrame(RHeel_raw, columns=['X', 'Y', 'Z'])
RHeel = tuple(RHeel.itertuples(index=False, name=None))

RToe_raw = calib_data['RToe']
RToe = pd.DataFrame(RToe_raw, columns=['X', 'Y', 'Z'])
RToe = tuple(RToe.itertuples(index=False, name=None))





### Trial Phase

# Load trial data
trial_data = TRCData()
trial_data.load(TRIAL_PATH)

# Load calibration matrices

# create proximal dynamic maker set

# create distal dynamic marker set

## Do Knee Joint Things
# create knee joint object
HipCenter = find_right_hip_center_andriacchi(RASIS=RASIS, RPSIS=RPSIS, LASIS=LASIS, LPSIS=LPSIS)
DynamicThighXAxis = ()
for idx, (i, j) in enumerate(zip(RKnee, RThigh)):
    DynamicThighXAxis += (i[0]-j[0], i[1]-j[1], i[2]-j[2]),
DynamicShankXAxis = ()
for idx, (i, j) in enumerate(zip(RAnkle, RShank)):
    DynamicShankXAxis += (i[0]-j[0], i[1]-j[1], i[2]-j[2]),
PBDMS = []
DBDMS = []
for idx, frame in enumerate(Frames):
    PBDMS.append(MarkerSet(RThigh[idx], DynamicThighXAxis[idx], HipCenter[idx]))
    DBDMS.append(MarkerSet(RShank[idx], DynamicShankXAxis[idx], RKnee[idx]))

# PBDMS = proximal dynamic marker set, DBDMS = distal dynamic marker set
Knee = Joint(PBDMS=PBDMS, DBDMS=DBDMS, proximal_bone_dynamic_to_true_matrix=, distal_bone_dynamic_to_true_matrix=)
#print(Knee.joint_angles)


# load the dynamic and true markersets into the thigh object
Thigh.load_markers(DynamicThigh, TrueThigh) # the markersets get loaded into the bone object and transformation matrices are created

# load in the actual trial data that we want to get info for
trial_data = TRCData()
trial_data.load('../friday/4407cd02.trc')   # cd02 is walking
# return movement in the true reference frame
final_data = np.matmul(Thigh.camera_to_local_matrix, trial_data)    # this trial_data needs to be broken down to the markers









