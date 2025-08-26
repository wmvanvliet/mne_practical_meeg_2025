# Material for the MNE-Python workshop of Practical MEEG 2022

More info on the workshop: [https://cuttingeeg.org/practicalmeeg2025](https://cuttingeeg.org/practicalmeeg2025)

Authors of the material:

    - Marijn van Vliet, Aalto University, Department of Neuroscience and Biomedical Engineering
	- Britta Westner, Radboud University Nijmegen, Donders Institute
	- Alexandre Gramfort, Inria, CEA Neurospin
	- Denis A. Engemann, Inria, CEA Neurospin

## Before you arrive

Please make sure you do the following steps before the first hands-on session:

0. You will need to download this directory of scripts.
1. You will need to [download the data](https://doi.org/10.5281/zenodo.7405048).
2. You will need to [download the extra data](https://drive.google.com/file/d/1EE_pDY-i6zkS5qiysaGw6HiG9yRLL1y1/view?usp=share_link) that we will use in some tutorials.
3. You will need to have an up-to-date version of MNE-Python installed on your machine (you need a *full install* with all dependencies, **not** "MNE-Python with core functionalities only"). See instructions at: https://mne.tools/stable/install/index.html
4. To check your installation, please look at the (very short!) notebook [Check your installation](0-Installation_check.ipynb). See below if you need a reminder how to start it.
5. If you are not familiar with Python, we invite you to take the time to work on these tutorials:
[Intro to Python](intro_to_python/0a-Intro_Python.ipynb), [Intro to Numpy](intro_to_python/0b-Intro_Numpy.ipynb).

### Start a Jupyter notebook

 To start a Jupyter notebook, open your terminal and navigate to the directory where you saved this directory of scripts. Then type the command `jupyter notebook` and Jupyter should open in your internet browser. Click on the notebook you want to run!


## Program

#### Day 0 (Monday October 27, 2025)

 - 14:00 - 15:30 Training cutting instructors
 - 15:30 - 15:40 Break
 - 15:40 – 17:30 Advanced training on MNE-Python

 - 17:30 – 18:00 Panel discussion

#### Day 1 (Tuesday October 28, 2025)

 - 08:30 – 09:00 Registration, with coffee/tea + Welcome & intro

 - 09:00 – 10:00 Lecture: Get to know your data: preprocessing, segmentation and artifacts
 - 10:00 - 10:10 Break
 - 10:10 – 12:00 Hands-on: [Preprocessing](1-Preprocessing.ipynb) using MNE-Python

 - 12:00 - 12:30 TrainEErs debriefing

 - 12:30 – 14:00 Lunch and posters

 - 14.00 – 15:30 Tune in to your frequency analysis
 - 15:30 - 15:40 Break
 - 15:40 – 17:30 Hands-on: [Sensor-level analysis](2-Time_domain_evoked_responses.ipynb) using MNE-Python
 - 15:40 – 17:30 Hands-on: [Time-frequency analysis](3-Time_frequency_analysis.ipynb) using MNE-Python

 - 17:00 – 17:30 Panel discussion
 - 17:30 - 18:00 CuttingGardens 2026

#### Day 3 (Wednesday October 29, 2025)

 - 09:00 – 10:30 Lecture: Source level analysis I: head and source level model and forward computation (Robert)
 - 10:30 - 10:40 Break
 - 10:40 – 12:00 Hands-on: [Forward modelling](4-Forward_modelling.ipynb) using MNE-Python

 - 12:00 - 12:30 TrainEErs debriefing

 - 12:30 – 14:00 Lunch and posters

 - 14:00 – 15:30 Lecture: Source level analysis II: getting to source level maps and time-series (Robert)
 - 15:30 - 15:40 Break
 - 15:40 - 17:00 Hands-on: [Source estimation](5-Source_reconstruction.ipynb) using MNE-Python

 - 17:00 – 17:30 Panel discussion
 - 17:30 – 18:00 CuttingStuff

#### Day 4 (Thursday October 30, 2025)

 - 09:00 – 10:30 Lecture: Get and report results with confidence I: univariate approach
 - 10:30 - 10:40 Break
 - 10:40 – 12:00 Hands-on: [Group level analysis](6-Group_analysis.ipynb) using MNE-Python

 - 12:00 - 12:30 TrainEErs debriefing

 - 12:30 – 14:00 Lunch and posters

 - 14.00 – 17:00 Toolbox Bouquet (online)
 - 17.00 – 18:00 AI use in MEG/EEG data analysis

 - 18:00 Social event

#### Day 5 (Friday October 31, 2025)

 - 09:00 – 10:30 Lecture: Get and report results with confidence II: multivariate approach
 - 10:30 - 10:40 Break
 - 10:40 – 12:00 Hands-on: [Multivariate analysis](7-Multivariate_analysis.ipynb) using MNE-Python

 - 12:00 - 12:30 TrainEErs debriefing


### References and credit

The code from this tutorial is heavily inspired from this article:

	Mainak Jas, Eric Larson, Denis Engemann, Jaakko Leppakangas, Samu Taulu, Matti Hamalainen,
	and Alexandre Gramfort. 2018. A Reproducible MEG/EEG Group Study With the MNE Software:
	Recommendations, Quality Assessments, and Good Practices.
	Frontiers in Neuroscience. 12, doi: 10.3389/fnins.2018.00530

The MNE software when used in publications should be acknowledged using citations.

To cite MNE-C or the inverse imaging implementations provided by the MNE software, please use:

	A. Gramfort, M. Luessi, E. Larson, D. Engemann, D. Strohmeier, C. Brodbeck, L. Parkkonen,
	M. Hämäläinen, MNE software for processing MEG and EEG data, NeuroImage, Volume 86,
	1 February 2014, Pages 446-460, ISSN 1053-8119.

To cite the MNE-Python package, please use:

	A. Gramfort, M. Luessi, E. Larson, D. Engemann, D. Strohmeier, C. Brodbeck, R. Goj, M. Jas,
	T. Brooks, L. Parkkonen, M. Hämäläinen, MEG and EEG data analysis with MNE-Python,
	Frontiers in Neuroscience, Volume 7, 2013, ISSN 1662-453X.

