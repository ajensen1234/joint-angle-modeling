"""
Main script for the project.
"""

# goal is to output the coorinates of the right thigh and right shank in the reference frames of the
# "true" hip and shank AKA the reference frames defined near the knee.

# import the necessary packages
from trc import TRCData
import pandas as pd
import numpy as np

from functions import *
from Bone import *

### VARIABLES
CALIB_MARKER_FRAME = 123

# load data
calib_data = TRCData()
calib_data.load('friday/4407cd01.trc')

"""
Try to combine the data into tuples all at once so we don't have a mess below.
"""

# General
Frames_raw = calib_data['Frame#']
Frames = pd.DataFrame(Frames_raw)

Time_raw = calib_data['Time']
Time = pd.DataFrame(Time_raw)

## Right Thigh
RASIS_raw = calib_data['RASIS']
RASIS = pd.DataFrame(RASIS_raw, columns=['X', 'Y', 'Z'])
RASIS = RASIS.to_numpy()

RPSIS_raw = calib_data['RPSIS']
RPSIS = pd.DataFrame(RPSIS_raw, columns=['X', 'Y', 'Z'])
RPSIS = RPSIS.to_numpy()

LASIS_raw = calib_data['LASIS']
LASIS = pd.DataFrame(LASIS_raw, columns=['X', 'Y', 'Z'])
LASIS = LASIS.to_numpy()

LPSIS_raw = calib_data['LPSIS']
LPSIS = pd.DataFrame(LPSIS_raw, columns=['X', 'Y', 'Z'])
LPSIS = LPSIS.to_numpy()

HipCenter = find_right_hip_center_andriacchi(RASIS=RASIS, RPSIS=RPSIS, LASIS=LASIS, LPSIS=LPSIS)

RThigh_raw = calib_data['RThigh']
RThigh = pd.DataFrame(RThigh_raw, columns=['X', 'Y', 'Z'])
RThigh = RThigh.to_numpy()

RKnee_raw = calib_data['RKnee']
RKnee = pd.DataFrame(RKnee_raw, columns=['X', 'Y', 'Z'])
RKnee = RKnee.to_numpy()

RMedKnee_raw = calib_data['RMed.Knee']
RMedKnee = pd.DataFrame(RMedKnee_raw, columns=['X', 'Y', 'Z'])
RMedKnee = RMedKnee.to_numpy()

RShank_raw = calib_data['RShank']
RShank = pd.DataFrame(RShank_raw, columns=['X', 'Y', 'Z'])
RShank = RShank.to_numpy()

RAnkle_raw = calib_data['RAnkle']
RAnkle = pd.DataFrame(RAnkle_raw, columns=['X', 'Y', 'Z'])
RAnkle = RAnkle.to_numpy()

RMedAnkle_raw = calib_data['RMed.Ankle']
RMedAnkle = pd.DataFrame(RMedAnkle_raw, columns=['X', 'Y', 'Z'])
RMedAnkle = RMedAnkle.to_numpy()

RHeel_raw = calib_data['RHeel']
RHeel = pd.DataFrame(RHeel_raw, columns=['X', 'Y', 'Z'])
RHeel = RHeel.to_numpy()

RToe_raw = calib_data['RToe']
RToe = pd.DataFrame(RToe_raw, columns=['X', 'Y', 'Z'])
RToe = RToe.to_numpy()


### Calibration Phase


## Do Thigh Things

# create dynamic ReferenceFrame object
DynamicThighXAxis = RKnee - RThigh
DynamicThigh = ReferenceFrame(origin=RThigh[CALIB_MARKER_FRAME], x_axis=DynamicThighXAxis[CALIB_MARKER_FRAME], z_prime_end=HipCenter[CALIB_MARKER_FRAME])

# create true ReferenceFrame object
TrueThighXAxis = RKnee - RMedKnee
TrueThighOrigin = MidPoint(RKnee, RMedKnee)
TrueThigh = ReferenceFrame(origin=TrueThighOrigin[CALIB_MARKER_FRAME], x_axis=TrueThighXAxis[CALIB_MARKER_FRAME], z_prime_end=HipCenter[CALIB_MARKER_FRAME])

# initialize thigh bone object
Thigh = Bone(dynamic_reference_frame=DynamicThigh, true_reference_frame=TrueThigh)


## Do Shank Things

#create dynamic ReferenceFrame object
DynamicShankXAxis = RAnkle - RShank
DynamicShank = ReferenceFrame(origin=RShank[CALIB_MARKER_FRAME], x_axis=DynamicShankXAxis[CALIB_MARKER_FRAME], z_prime_end=RKnee[CALIB_MARKER_FRAME])

# create true ReferenceFrame object
TrueShankXAxis = RKnee - RMedKnee
TrueShankOrigin = TrueThighOrigin
TrueShank = ReferenceFrame(origin=TrueShankOrigin[CALIB_MARKER_FRAME], x_axis=TrueShankXAxis[CALIB_MARKER_FRAME], z_prime_end=RAnkle[CALIB_MARKER_FRAME])

# initialize shank bone object
Shank = Bone(dynamic_reference_frame=DynamicShank, true_reference_frame=TrueShank)


# Save calibration matrices
proximal_bone_dynamic_to_true_matrix = Thigh.dynamic_to_true_matrix
proximal_bone_dynamic_to_true_matrix.dump("proximal_bone_dynamic_to_true_matrix.npy")

distal_bone_dynamic_to_true_matrix = Shank.dynamic_to_true_matrix
distal_bone_dynamic_to_true_matrix.dump("distal_bone_dynamic_to_true_matrix.npy")












