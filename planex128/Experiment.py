from solvers.Solver2StageRGBD_6DoF import *
from models.filetools import *
from solvers.tools.quattool import *



class Experiment:
    """Universal class to run CNN model experiments.
    The class gets a description from a dictionary and can run the experiment with this
    description.

    Rafael Radkowski
    Iowa State University
    rafael@iastate.edu
    +1 (515) 294-7044
    MIT License
    Aug 8, 2019

    """

    _descrip = []
    _ready = False

    def __init__(self, description):
        """ Init the class with a description of the experiment.

        :param description: dictionary
        The dictionary must contain the following variables
        train_dataset: (string) the training dataset path and file, e.g., "../data/dataset_bunny06.pickle"
        test_dataset: (string) the test dataset e.g,., "../data/dataset_bunny06.pickle"
        solver: (class) the class of the solver to be user, e.g., SolverRGBD_QuatLoss
        model: (class) the class name of the CNN model to be used, e.g.,  Model_RGBD_6DoF_L
        num_iterations: (integer) containing the number of iterations to run, e.g., 100
        learning_rate: (float) Learning rate for the model
        debug_output: (bool) if True, graphical debug windows are display, False hides them.
        log_path: (string) relative or absolute log path. END THE PATH WITH A "/", e.g., "./log/23/"
        log_file: (string) a file name for a log file, e.g., "bunny06_64x64"
        train: (bool) set True to enable training, False will not train the model
        eval: (bool) set True to enable x-evaluation after training, False will not eval the model
        test: (bool) set True to test model with the test_dataset. Note that the variable test_dataset must be set
        restore_file: (string) filename of the model that needs to be restored. Keep empty to train from scratch.
        quat_used: (bool) indicate if the dataset contains quaternions. Set to True, if so.
        plot_title: (string) a string containing a title that should appear on the plot.
        """
        self._descrip = description

        # check the dictionary for completeness
        err = self.__check_dict__( self._descrip )

        if err == 2:
            self._ready = False
            print("ABORT - CRITICAL ERRORS. CNN WILL NOT RUN")
        else:
            self._ready = True

    def start(self):
        """
        Start the experiment
        :return:
        """

        if self._ready == False:
            return

        # Load and prepare the data
        # [Xtr, Xtr_depth, Ytr, Ytr_pose, Xte, Xte_depth, Yte, Yte_pose]
        loaded_data = prepare_data_RGBD_6DoF(self._descrip["train_dataset"])

        # Synthetic data
        Xtr_rgb = loaded_data[0]
        Xtr_depth = loaded_data[1]
        Ytr_mask = loaded_data[2]
        Ytr_pose = loaded_data[3]  # [:,0]
        # convert all quaternions into axis-angle transformation
        Ytr_pose_aa = []
        size = Ytr_pose.shape[0]
        for i in range(0, size):
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
        # Ytr_pose[:,[3,6]] = Ytr_pose[:,[6,3]]

        Xte_rgb = loaded_data[4]
        Xte_depth = loaded_data[5]
        Yte_mask = loaded_data[6]
        Yte_pose = loaded_data[7]  # [:,0]
        Yte_pose_aa = []
        size = Yte_pose.shape[0]
        for i in range(0, size):
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
        # Yte_pose[:,[3,6]] = Yte_pose[:,[6,3]]


        # Init the network
        solver = self._descrip["solver"](self._descrip["model"], 2, 3, 4, self._descrip["learning_rate"])
        solver.setParams(self._descrip["num_iterations"], 128, 128)
        solver.showDebug(self._descrip["debug_output"])
        solver.setLogPathAndFile(self._descrip["log_path"], self._descrip["log_file"])

        # start training
        solver.init(Xtr_rgb.shape[1], Xtr_rgb.shape[2], self._descrip["restore_file"])
        solver.img_dimensions(Xtr_rgb.shape[1], Xtr_rgb.shape[2])
        if self._descrip["train"]:
            solver.train( Xtr_rgb, Xtr_depth, Ytr_mask, Ytr_pose, Xte_rgb, Xte_depth, Yte_mask, Yte_pose)

        # evaluate
        if self._descrip["eval"]:
            solver.eval(Xte_rgb, Xte_depth, Yte_mask, Yte_pose)

        # evaluation with a second evaluation set.
        if self._descrip["test"] and len(self._descrip["test_dataset"]) > 0:
            # Real world evaluation data
            loaded_eval_data = prepare_data_RGBD_6DoF(self._descrip["test_dataset"])
            Xev_rgb = loaded_eval_data[0]
            Xev_depth = loaded_eval_data[1]
            Yev_mask = loaded_eval_data[2]
            Yev_pose = loaded_eval_data[3]  # [:,0]

            # swap colums for the quaternion from (x, y, z, w) -> (w, x, y, z)
            # Yev_pose[:,[3,6]] = Yev_pose[:,[6,3]]
            solver.eval(Xev_rgb, Xev_depth, Yev_mask, Yev_pose)

        # # Analyze the results
        # da = DataAnalysis()
        # da.setModelParam(str(self._descrip["model"]), str(self._descrip["solver"]), self._descrip["label"])
        # da.setExpParam(self._descrip["train_dataset"], Xtr_rgb.shape[0], Xte_rgb.shape[0], self._descrip["num_iterations"])
        # da.analyze(self._descrip["log_path"], self._descrip["log_path"], self._descrip["plot_title"], self._descrip["quat_used"], False)



    def __check_dict__(self, dict):
        """Check if all keys are present

        The function compares the given keys with a set of expected keys and tries to fix them if
        possible.

        :param dict: (dict)
            Dictionary with all keys.
        :return: (int)
            An error code.
            0 - no errors
            1 - some solveable errors
            2 - critical error - abort
        """
        error_level = 0

        expected_keys = ["train_dataset", "test_dataset", "solver", "model", "num_iterations", "debug_output", "log_path",
                         "log_file", "train", "eval", "test", "restore_file", "quat_used", "plot_title",
                         "learning_rate", "label"]

        keys = dict.keys()

        # search for all keys.
        for i in keys:
            for j in expected_keys:
                if i == j:
                    expected_keys.remove(i)
                    break

        # Check the missing variables and try to fix them
        if len(expected_keys) > 0:
            print("WARNING - Not all variables have been set. Miss the following variables")
            for i in expected_keys:
                print(i + ", ")

            for i in expected_keys:
                if i == "train_dataset":
                    print("CRITICAL ERROR - Training dataset is missing!")
                    error_level = 2
                elif i == "test_dataset":
                    print("Test dataset is missing, disable tests")
                    self._descrip["test"] = False
                elif i == "solver":
                    print("CRITICAL ERROR - Solver is missing!")
                    error_level = 2
                elif i == "model":
                    print("CRITICAL ERROR - Model is missing!")
                    error_level = 2
                elif i == "num_iterations":
                    print("num_iterations is missing! Set to 100")
                    self._descrip["num_iterations"] = 100
                elif i == "debug_output":
                    print("debug_output of iteratrion is missing! Set to False")
                    self._descrip["debug_output"] = False
                elif i == "log_path":
                    print("log_path is missing! Set to ./logs/temp/")
                    self._descrip["log_path"] = "./logs/temp/"
                elif i == "log_file":
                    print("log_file is missing! Set to idiot")
                    self._descrip["log_file"] = "idiot"
                elif i == "train":
                    print("train is missing! Set to True")
                    self._descrip["train"] = True
                elif i == "eval":
                    print("eval is missing! Set to True")
                    self._descrip["eval"] = True
                elif i == "test":
                    print("test is missing! Set to False")
                    self._descrip["test"] = False
                elif i == "restore_file":
                    print("restore_file is missing! Set empty string")
                    self._descrip["restore_file"] = ""
                elif i == "quat_used":
                    print("quat_used is missing! Set to True")
                    self._descrip["restore_file"] = True
                elif i == "plot_title":
                    print("plot_title is missing! Set to No Title")
                    self._descrip["plot_title"] = "No title"
                elif i == "learning_rate":
                    print("learning_rate is missing! Set to 0.001")
                    self._descrip["learning_rate"] = 0.001
                elif i == "label":
                    self._descrip["label"] = "Unlabeled experiment"


        return error_level