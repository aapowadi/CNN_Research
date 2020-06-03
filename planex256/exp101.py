import tensorflow as tf
import numpy as np
import pickle
import cv2
from models.Model_RGBD_6DoF import *
#from models.Model_RGBD_6DoF_L import *
from solvers.Solver2StageRGBD_6DoF import *
from models.filetools import *
from solvers.tools.quattool import *

"""----------------------------------------------------------------------------
    CNN for 6 DoF Pose estimation No. 3

    This file controls an experiment for pose estimation with
    RGB and depth data. 
    The RGB data is used to segment to object of interest.
    The segmented region is augmented with depth data and the pose, 
    given as translation and quaternion, is estimated by two subsequent networks.

    The pose is represented as translation (x,y,z) and as a 4-component axis-angle orientation (rx, ry, rz, ang).
    The length of the axis encodes the angle in radians. 
    
    Purpose:
    - Experiments with the transducer

    Rafael Radkowski
    Iowa State University
    rafael@iastate.edu
    515 294 7044
    June 28, 2019
    MIT License

    -------------------------------------------
    Edits:

"""

""" ---------------------------------------------
Test and training parameters 
"""

# Data file
FILE = "../../datasets/cnn-ground_truth.pickle"
FILE_EVAL = "../../datasets/cnn-ground_truth.pickle"

# Log file
log_folder = "./log/101/"
log_file = "cnn_gtx64"


# Restore, set a name to restore the data from a file
restore_file = ""

# Load and prepare the data
# [Xtr, Xtr_depth, Ytr, Ytr_pose, Xte, Xte_depth, Yte, Yte_pose]
loaded_data = prepare_data_RGBD_6DoF(FILE)

# Synthetic data
Xtr_rgb = loaded_data[0]
Xtr_depth = loaded_data[1]
Ytr_mask = loaded_data[2]
# for i in range (len(Ytr_mask)):
#    img = Ytr_mask[i:i +1];
#    img = img.reshape([1,img.shape[1],img.shape[2]]);
Ytr_pose = loaded_data[3]#[:,0]

# convert all quaternions into axis-angle transformation
Ytr_pose_aa = []
size = Ytr_pose.shape[0]
for i in range(0,size):
    pose = Ytr_pose[i]
    t = pose[0:3]
    q = pose[3:7]
    aa = Quaternion.quat2AxisAngle(q)
    new_pose = np.array([t[0], t[1], t[2], float(aa[0]), float(aa[1]), float(aa[2]), float(aa[3])])
    new_pose = new_pose.reshape([1, new_pose.shape[0]])
    if i == 0:
        Ytr_pose_aa = new_pose
    else:
        Ytr_pose_aa = np.concatenate((Ytr_pose_aa, new_pose), axis=0)


# swap colums for the quaternion from (x, y, z, w) -> (w, x, y, z)
#Ytr_pose[:,[3,6]] = Ytr_pose[:,[6,3]]

#Ytr_pose = np.resize(Ytr_pose, [18000,1])

Xte_rgb = loaded_data[4]
Xte_depth = loaded_data[5]
Yte_mask = loaded_data[6]
Yte_pose = loaded_data[7]#[:,0]
#Yte_pose = np.resize(Yte_pose, [2000,1])

Yte_pose_aa = []
size = Yte_pose.shape[0]
for i in range(0,size):
    pose = Yte_pose[i]
    t = pose[0:3]
    q = pose[3:7]
    aa = Quaternion.quat2AxisAngle(q)
    new_pose = np.array([t[0], t[1], t[2], float(aa[0]), float(aa[1]), float(aa[2]), float(aa[3])])
    new_pose = new_pose.reshape([1, new_pose.shape[0]])
    if i == 0:
        Yte_pose_aa = new_pose
    else:
        Yte_pose_aa = np.concatenate((Yte_pose_aa, new_pose), axis=0)

# swap colums for the quaternion from (x, y, z, w) -> (w, x, y, z)
#Yte_pose[:,[3,6]] = Yte_pose[:,[6,3]]

# Real world evaluation data
loaded_eval_data = prepare_data_RGBD_6DoF(FILE_EVAL)
Xev_rgb = loaded_eval_data[0]
Xev_depth = loaded_eval_data[1]
Yev_mask = loaded_eval_data[2]
Yev_pose = loaded_eval_data[3]#[:,0]

# swap colums for the quaternion from (x, y, z, w) -> (w, x, y, z)
#Yev_pose[:,[3,6]] = Yev_pose[:,[6,3]]


# Init the network
solver = Solver2StageRGBD_6DoF(Model_RGBD_6DoF, 2, 3, 4, 0.001)
solver.setParams(200, 128, 256)
solver.showDebug( True)
solver.setLogPathAndFile(log_folder, log_file)

# start training
solver.init(Xtr_rgb.shape[1], Xtr_rgb.shape[2], restore_file)
solver.train(Xtr_rgb, Xtr_depth, Ytr_mask, Ytr_pose_aa, Xte_rgb, Xte_depth, Yte_mask, Yte_pose_aa)

# evaluate
#solver.eval(Xte_rgb, Xte_depth, Yte_mask, Yte_pose_aa)
#solver.eval(Xev_rgb, Xev_depth, Yev_mask, Yev_pose)