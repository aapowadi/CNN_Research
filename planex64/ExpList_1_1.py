#from solvers.SolverRGBD_QuatLoss import *
from models.Model_4 import *
from models.Model_8 import *
from models.Model_10 import *
from solvers.Solver2StageRGBD_6DoF import *


# This experiment works with the bunny model 64 x 64 pixels.
# The model color is adapted (chromatic adaptation) and noise was applied with sigma = 0.15
#
Exp1 = {}
Exp1["train_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp1["test_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp1["solver"] = Solver2StageRGBD_6DoF
Exp1["model"] = Model_4
Exp1["learning_rate"] = 0.001
Exp1["num_iterations"] = 300
Exp1["debug_output"] = True
Exp1["log_path"] = "./log/101/"
Exp1["log_file"] = "planex64"
Exp1["train"] = True
Exp1["eval"] = False
Exp1["test"] = False
Exp1["restore_file"] = ""  # keep empty to not restore a model.
Exp1["quat_used"] = False  # set true, if the dataset contains quaternions. Otherwise false.
Exp1["plot_title"] = "planex64_exp1 color, noise"
Exp1["label"] = "Experiment.py"

Exp2 = {}
Exp2["train_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp2["test_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp2["solver"] = Solver2StageRGBD_6DoF
Exp2["model"] = Model_4
Exp2["learning_rate"] = 0.01
Exp2["num_iterations"] = 300
Exp2["debug_output"] = True
Exp2["log_path"] = "./log/102/"
Exp2["log_file"] = "planex64"
Exp2["train"] = True
Exp2["eval"] = False
Exp2["test"] = False
Exp2["restore_file"] = ""  # keep empty to not restore a model.
Exp2["quat_used"] = False  # set true, if the dataset contains quaternions. Otherwise false.
Exp2["plot_title"] = "planex64_exp2 color, noise"
Exp2["label"] = "Experiment.py"

Exp3 = {}
Exp3["train_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp3["test_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp3["solver"] = Solver2StageRGBD_6DoF
Exp3["model"] = Model_4
Exp3["learning_rate"] = 0.1
Exp3["num_iterations"] = 300
Exp3["debug_output"] = True
Exp3["log_path"] = "./log/103/"
Exp3["log_file"] = "planex64"
Exp3["train"] = True
Exp3["eval"] = False
Exp3["test"] = False
Exp3["restore_file"] = ""  # keep empty to not restore a model.
Exp3["quat_used"] = False  # set true, if the dataset contains quaternions. Otherwise false.
Exp3["plot_title"] = "planex64_exp3 color, noise"
Exp3["label"] = "Experiment.py"

# This experiment works with the bunny model 64 x 64 pixels.
# The model color is adapted (chromatic adaptation) and noise was applied with sigma = 0.15
#
Exp4 = {}
Exp4["train_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp4["test_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp4["solver"] = Solver2StageRGBD_6DoF
Exp4["model"] = Model_8
Exp4["learning_rate"] = 0.001
Exp4["num_iterations"] = 300
Exp4["debug_output"] = True
Exp4["log_path"] = "./log/104/"
Exp4["log_file"] = "planex64"
Exp4["train"] = True
Exp4["eval"] = False
Exp4["test"] = False
Exp4["restore_file"] = ""  # keep empty to not restore a model.
Exp4["quat_used"] = False  # set true, if the dataset contains quaternions. Otherwise false.
Exp4["plot_title"] = "planex64_Exp4 color, noise"
Exp4["label"] = "Experiment.py"

Exp5 = {}
Exp5["train_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp5["test_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp5["solver"] = Solver2StageRGBD_6DoF
Exp5["model"] = Model_8
Exp5["learning_rate"] = 0.01
Exp5["num_iterations"] = 300
Exp5["debug_output"] = True
Exp5["log_path"] = "./log/105/"
Exp5["log_file"] = "planex64"
Exp5["train"] = True
Exp5["eval"] = False
Exp5["test"] = False
Exp5["restore_file"] = ""  # keep empty to not restore a model.
Exp5["quat_used"] = False  # set true, if the dataset contains quaternions. Otherwise false.
Exp5["plot_title"] = "planex64_Exp5 color, noise"
Exp5["label"] = "Experiment.py"

Exp6 = {}
Exp6["train_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp6["test_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp6["solver"] = Solver2StageRGBD_6DoF
Exp6["model"] = Model_8
Exp6["learning_rate"] = 0.1
Exp6["num_iterations"] = 300
Exp6["debug_output"] = True
Exp6["log_path"] = "./log/106/"
Exp6["log_file"] = "planex64"
Exp6["train"] = True
Exp6["eval"] = False
Exp6["test"] = False
Exp6["restore_file"] = ""  # keep empty to not restore a model.
Exp6["quat_used"] = False  # set true, if the dataset contains quaternions. Otherwise false.
Exp6["plot_title"] = "planex64_Exp6 color, noise"
Exp6["label"] = "Experiment.py"

# This experiment works with the bunny model 64 x 64 pixels.
# The model color is adapted (chromatic adaptation) and noise was applied with sigma = 0.15
#
Exp7 = {}
Exp7["train_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp7["test_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp7["solver"] = Solver2StageRGBD_6DoF
Exp7["model"] = Model_10
Exp7["learning_rate"] = 0.001
Exp7["num_iterations"] = 300
Exp7["debug_output"] = True
Exp7["log_path"] = "./log/107/"
Exp7["log_file"] = "planex64"
Exp7["train"] = True
Exp7["eval"] = False
Exp7["test"] = False
Exp7["restore_file"] = ""  # keep empty to not restore a model.
Exp7["quat_used"] = False  # set true, if the dataset contains quaternions. Otherwise false.
Exp7["plot_title"] = "planex64_Exp7 color, noise"
Exp7["label"] = "Experiment.py"

Exp8 = {}
Exp8["train_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp8["test_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp8["solver"] = Solver2StageRGBD_6DoF
Exp8["model"] = Model_10
Exp8["learning_rate"] = 0.01
Exp8["num_iterations"] = 300
Exp8["debug_output"] = True
Exp8["log_path"] = "./log/108/"
Exp8["log_file"] = "planex64"
Exp8["train"] = True
Exp8["eval"] = False
Exp8["test"] = False
Exp8["restore_file"] = ""  # keep empty to not restore a model.
Exp8["quat_used"] = False  # set true, if the dataset contains quaternions. Otherwise false.
Exp8["plot_title"] = "planex64_Exp8 color, noise"
Exp8["label"] = "Experiment.py"

Exp9 = {}
Exp9["train_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp9["test_dataset"] = "../../datasets/tr-probe-64.pickle"
Exp9["solver"] = Solver2StageRGBD_6DoF
Exp9["model"] = Model_10
Exp9["learning_rate"] = 0.1
Exp9["num_iterations"] = 300
Exp9["debug_output"] = True
Exp9["log_path"] = "./log/109/"
Exp9["log_file"] = "planex64"
Exp9["train"] = True
Exp9["eval"] = False
Exp9["test"] = False
Exp9["restore_file"] = ""  # keep empty to not restore a model.
Exp9["quat_used"] = False  # set true, if the dataset contains quaternions. Otherwise false.
Exp9["plot_title"] = "planex64_Exp9 color, noise"
Exp9["label"] = "Experiment.py"
