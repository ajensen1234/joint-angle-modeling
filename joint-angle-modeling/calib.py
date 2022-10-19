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

### VARIABLES
CALIB_MARKER_FRAME = 123

# load data
calib_data = TRCData()
calib_data.load('../friday/4407cd01.trc')

"""
Try to combine the data into tuples all at once so we don't have a mess below.
"""

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


### Calibration Phase


## Do Thigh Things

# create dynamic markerset object
HipCenter = find_right_hip_center_andriacchi(RASIS=RASIS, RPSIS=RPSIS, LASIS=LASIS, LPSIS=LPSIS)
DynamicThighXAxis = ()
for idx, (i, j) in enumerate(zip(RKnee, RThigh)):
    DynamicThighXAxis += (i[0] - j[0], i[1] - j[1], i[2] - j[2]),
DynamicThigh = MarkerSet(origin=RThigh[CALIB_MARKER_FRAME], x_axis=DynamicThighXAxis[CALIB_MARKER_FRAME], z_prime_end=HipCenter[CALIB_MARKER_FRAME])

# create true markerset object
# TrueThigh = MarkerSet(RKnee, RMedKnee, HipCenter)
# TrueThigh = MarkerSet(origin, x_axis, z_prime_axis)
TrueThighXAxis = ()
for idx, (i, j) in enumerate(zip(RKnee, RMedKnee)):
    TrueThighXAxis += (i[0] - j[0], i[1] - j[1], i[2] - j[2]),
TrueThighOrigin = MidPoint(RKnee, RMedKnee)
TrueThigh = MarkerSet(origin=TrueThighOrigin[CALIB_MARKER_FRAME], x_axis=TrueThighXAxis[CALIB_MARKER_FRAME], z_prime_axis=HipCenter[CALIB_MARKER_FRAME])

# initialize thigh bone object
Thigh = Bone(dynamic_marker_set=DynamicThigh, true_marker_set=TrueThigh)


## Do Shank Things

#create dynamic markerset object
DynamicShankXAxis = ()
for idx, (i, j) in enumerate(zip(RAnkle, RShank)):
    DynamicShankXAxis += (i[0]-j[0], i[1]-j[1], i[2]-j[2]),
DynamicShank = MarkerSet(origin=RShank[CALIB_MARKER_FRAME], x_axis=DynamicShankXAxis[CALIB_MARKER_FRAME], z_prime_axis=RKnee[CALIB_MARKER_FRAME])

# create true markerset object
TrueShankXAxis = ()
for idx, (i, j) in enumerate(zip(RKnee, RMedKne)):
    TrueShankXAxis += (i[0]-j[0], i[1]-j[1], i[2]-j[2]),
TrueShankOrigin = TrueThighOrigin
TrueShank = MarkerSet(origin=TrueShankOrigin[CALIB_MARKER_FRAME], x_axis=TrueShankXAxis[CALIB_MARKER_FRAME], z_prime_axis=RAnkle[CALIB_MARKER_FRAME])

# initialize shank bone object
Shank = Bone(dynamic_marker_set=DynamicShank, true_marker_set=TrueShank)


# Save calibration matrices














